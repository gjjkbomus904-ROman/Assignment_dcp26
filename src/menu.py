from datetime import date, datetime
import analysis
import charts
import db
import queries


def show_entries(conn):
    #The user can filter by category and by start date
    df = analysis.load_data(conn)
    categories = ", ".join(sorted(df["category"].unique()))
    category = input("Category (" + categories + "; Enter = all): ").strip()
    if category:
        df = df[df["category"].str.lower() == category.lower()]

    start = input("From date YYYY-MM-DD (Enter = from the beginning): ").strip()
    if start != "":
        try:
            datetime.strptime(start, "%Y-%m-%d")  # check that it looks like a date
            df = df[df["date"] >= start]
        except ValueError:
            print("That is not a date, so I did not filter by date.")

    columns = ["date", "weekday", "activity", "category", "duration_hours", "notes"]
    print(df[columns].to_string(index=False))
    print(len(df), "entries,", df["duration_hours"].sum(), "hours")


def run_sql(conn):
    #Let the user choose one of the SQL queries
    for number, (title, sql) in enumerate(queries.QUERIES, start=1):
        print(number, "-", title)
    choice = input("Query number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(queries.QUERIES):
        title, sql = queries.QUERIES[int(choice) - 1]
        queries.run(conn, title, sql)
    else:
        print("Please type a number from the list.")


def show_analysis(conn):
    #Print the results of the pandas analysis
    df = analysis.load_data(conn)
    analysis.print_summary(df)


def show_charts(conn):
    df = analysis.load_data(conn)
    for number, (name, function) in enumerate(charts.CHARTS, start=1):
        print(number, "-", name)
    choice = input("Chart number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(charts.CHARTS):
        name, function = charts.CHARTS[int(choice) - 1]
        function(df)
        print("Chart saved in the charts folder.")
    else:
        print("Please type a number from the list.")


def add_row(conn):
    #Ask for a new entry and save it
    print("Add an entry. Write only what really happened.")
    day = input("Date (Enter = today): ").strip()
    if day == "":
        day = str(date.today())
    activity = input("Activity (for example Working): ").strip()
    category = input("Category (Work, Study, Social, Meeting, Sport, Trip, Leisure): ").strip()
    hours = input("Duration in hours: ").strip().replace(",", ".")
    notes = input("Notes: ").strip()

    problem = db.add_entry(conn, day, activity, category, hours, notes)
    if problem:
        print("Not saved:", problem)
    else:
        print("Saved to the CSV file and the database. Commit the CSV to GitHub today.")


conn = db.connect()
loaded, rejected = db.load_csv(conn)
print("Loaded", loaded, "rows from the CSV file.")
for line_number, problem in rejected:
    print("Rejected line", line_number, "-", problem)

while True:
    print()
    print("=== My Time Tracker ===")
    print("1 - Show entries")
    print("2 - Run an SQL query")
    print("3 - Analysis")
    print("4 - Charts")
    print("5 - Add an entry")
    print("0 - Exit")
    choice = input("Choose: ").strip()

    if choice == "1":
        show_entries(conn)
    elif choice == "2":
        run_sql(conn)
    elif choice == "3":
        show_analysis(conn)
    elif choice == "4":
        show_charts(conn)
    elif choice == "5":
        add_row(conn)
    elif choice == "0":
        break
    else:
        print("Please type a number from the menu.")

conn.close()