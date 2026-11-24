import db


def run(conn, title, sql):
    """Run one query and print the result."""
    print()
    print(title)
    cursor = conn.execute(sql)
    print([item[0] for item in cursor.description])  # column names
    for row in cursor.fetchall():
        print(row)


conn = db.connect()
db.load_csv(conn) #load and connect CSV file

run(conn, "Total hours per category", """
    Select category, count(*), sum(duration_hours)
    From activities
    Group by category
    Order by Sum(duration_hours) DESC
""")

run(conn, "The 5 days with the most hours", """
    Select date, Sum(duration_hours)
    From activities
    Group by date
    Order by Sum(duration_hours) DESC
    Limit 5
""")

run(conn, "Work entries of 9 hours or more", """
    Select date, activity, duration_hours
    From activities
    Where category = 'Work' and duration_hours >= 9
""")

run(conn, "Work and study: total hours and number of days", """
    Select category, Sum(duration_hours), Count(Distinct date)
    From activities
    Where category in ('Work', 'Study')
    Group by category
""")

run(conn, "Average length of one entry per category", """
    Select category, Round(AVG(duration_hours), 1)
    From activities
    Group by category
    Order by AVG(duration_hours) DESC
""")

conn.close()
