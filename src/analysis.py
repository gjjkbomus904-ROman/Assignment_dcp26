import pandas as pd
import db

def load_data(conn):
    df = pd.read_sql("Select * From activities", conn, parse_dates=["date"])
    df["weekday"] = df["date"].dt.day_name()
    df["is_weekend"] = df["date"].dt.dayofweek >= 5  # 5 = Saturday, 6 = Sunday
    return df


def category_summary(df):
    #Number of entries, total hours and average hours for each category
    summary = df.groupby("category")["duration_hours"].agg(["count", "sum", "mean"])
    summary["share_percent"] = summary["sum"] / summary["sum"].sum() * 100
    return summary.sort_values("sum", ascending=False)


def weekday_vs_weekend(df):
    #Days, total hours and hours per day. False = weekday, True = weekend
    per_day = df.groupby(["date", "is_weekend"])["duration_hours"].sum().reset_index()
    return per_day.groupby("is_weekend")["duration_hours"].agg(["count", "sum", "mean"])


def work_study_per_day(df):
    #Work hours and study hours for each day
    daily = df.pivot_table(index="date", columns="category",
                           values="duration_hours", aggfunc="sum", fill_value=0)
    daily = daily[["Work", "Study"]]
    return daily[(daily["Work"] > 0) | (daily["Study"] > 0)]


def weekly_hours(df):
    #Hours per week and category
    df = df.copy()
    df["week"] = df["date"].dt.to_period("W").dt.start_time.dt.date
    return df.pivot_table(index="week", columns="category",
                          values="duration_hours", aggfunc="sum", fill_value=0)


def print_summary(df):
    """Print all the results of the analysis."""
    print("\nBy category")
    print(category_summary(df).round(1))

    print("\nWeekday (False) vs weekend (True)")
    print(weekday_vs_weekend(df).round(1))

    totals = df.groupby("date")["duration_hours"].sum()
    print("\nBusiest day:", totals.idxmax().date(), totals.max(), "hours")
    print("Quietest day:", totals.idxmin().date(), totals.min(), "hours")

    daily = work_study_per_day(df)
    print("\nCorrelation of work and study:", round(daily["Work"].corr(daily["Study"]), 2))

    print("\nHours per week")
    print(weekly_hours(df))


if __name__ == "__main__":
    conn = db.connect()
    db.load_csv(conn)
    df = load_data(conn)
    conn.close()
    print_summary(df)
