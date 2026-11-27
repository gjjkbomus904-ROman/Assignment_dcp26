"""Load my time data from the CSV file into a SQLite database."""
import csv
import sqlite3
from datetime import datetime

CSV_PATH = "data/time_spending.csv"
DB_PATH = "data/time_spending.db"


def connect():
    """Open the database"""
    return sqlite3.connect(DB_PATH)


def create_table(conn):
    """Create the activities table. It is deleted first, so it is always rebuilt."""
    conn.execute("DROP TABLE IF EXISTS activities")
    conn.execute("""
        CREATE TABLE activities (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            date           TEXT NOT NULL,
            activity       TEXT NOT NULL,
            category       TEXT NOT NULL,
            duration_hours REAL NOT NULL,
            notes          TEXT
        )
    """)


def check_row(row):
    """Check one row from the CSV. Returns a text with the problem, or None if it is ok."""
    # the date must look like 2026-10-19
    try:
        datetime.strptime(row["date"], "%Y-%m-%d")
    except ValueError:
        return "bad date: " + row["date"]

    # activity and category must not be empty
    if row["activity"].strip() == "" or row["category"].strip() == "":
        return "empty activity or category"

    # the duration must be a number between 0 and 24
    try:
        hours = float(row["duration_hours"])
    except ValueError:
        return "duration is not a number: " + row["duration_hours"]
    if hours <= 0 or hours > 24:
        return "duration out of range: " + str(hours)

    return None


def load_csv(conn):
    """Read the CSV and put every good row into the table.
    Returns the number of loaded rows and a list of the rejected rows """
    create_table(conn)
    loaded = 0
    rejected = []

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        line_number = 1  # line 1 is the header
        for row in reader:
            line_number += 1
            problem = check_row(row)
            if problem:
                rejected.append((line_number, problem))
                continue
            conn.execute(
                "INSERT INTO activities (date, activity, category, duration_hours, notes) "
                "VALUES (?, ?, ?, ?, ?)",
                (row["date"], row["activity"], row["category"],
                 float(row["duration_hours"]), row["notes"]),
            )
            loaded += 1

    conn.commit()
    return loaded, rejected

def add_entry(conn, date, activity, category, hours, notes):
    #Add one new row to the CSV file and to the database.

    #Returns a text with the problem if the row is not valid, otherwise None
    row = {"date": date, "activity": activity, "category": category,
           "duration_hours": hours, "notes": notes}
    problem = check_row(row)
    if problem:
        return problem

    # make sure the last line of the CSV ends with a new line before adding to it
    with open(CSV_PATH, "rb") as f:
        text = f.read()
    if not text.endswith(b"\n"):
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            f.write("\r\n")

    # the CSV is the main file, so the row goes there first
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([date, activity, category, hours, notes])

    conn.execute(
        "INSERT INTO activities (date, activity, category, duration_hours, notes) "
        "VALUES (?, ?, ?, ?, ?)",
        (date, activity, category, float(hours), notes),
    )
    conn.commit()
    return None

if __name__ == "__main__":
    conn = connect()
    loaded, rejected = load_csv(conn)
    print("Loaded rows:", loaded)
    for line_number, problem in rejected:
        print("Rejected line", line_number, "-", problem)

    # count the rows and add up the hours in the database
    rows, hours = conn.execute(
        "Select count(*), Sum(duration_hours) From activities").fetchone()
    print("In the database:", rows, "rows,", hours, "hours")
    conn.close()