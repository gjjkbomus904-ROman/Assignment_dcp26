import db

#title and the SQL text
QUERIES = [
    ("Total hours per category", """
        Select category, Count(*), Sum(duration_hours)
        From activities
        Group by category
        Order by Sum(duration_hours) DESC
    """),
    ("The 5 days with the most hours", """
        Select date, Sum(duration_hours)
        From activities
        Group by date
        Order by Sum(duration_hours) DESC
        Limit 5
    """),
    ("Work entries of 9 hours or more", """
        Select date, activity, duration_hours
        From activities
        Where category = 'Work' and duration_hours >= 9
    """),
    ("Work and study: total hours and number of days", """
        Select category, Sum(duration_hours), Count(DISTINCT date)
        From activities
        Where category in ('Work', 'Study')
        Group by category
    """),
    ("Average length of one entry per category", """
        Select category, Round(AVG(duration_hours), 1)
        From activities
        Group by category
        Order by AVG(duration_hours) DESC
    """),
]


def run(conn, title, sql):
    #Run one query and print the result
    print()
    print(title)
    cursor = conn.execute(sql)
    print([item[0] for item in cursor.description])  # column names
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    conn = db.connect()
    db.load_csv(conn)
    for title, sql in QUERIES:
        run(conn, title, sql)
    conn.close()