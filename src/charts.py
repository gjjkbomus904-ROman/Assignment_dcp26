import os
import matplotlib.pyplot as plt
import analysis

def save_and_show(file_name):
    #Save the chart as a picture in the charts folder and show it
    os.makedirs("charts", exist_ok=True)
    plt.tight_layout()
    plt.savefig("charts/" + file_name)
    plt.show()
    plt.close()


def chart_categories(df):
    hours = df.groupby("category")["duration_hours"].sum().sort_values(ascending=False)
    hours.plot(kind="bar", rot=0)
    plt.title("Recorded hours per category")
    plt.ylabel("Hours")
    save_and_show("hours_by_category.png")


def chart_daily(df):
    totals = df.groupby("date")["duration_hours"].sum()
    totals.plot(marker="o", rot=45)
    plt.title("Recorded hours per day")
    plt.ylabel("Hours")
    save_and_show("total_day.png")


def chart_weekday(df):
    per_day = df.groupby(["date", "weekday"])["duration_hours"].sum().reset_index()
    average = per_day.groupby("weekday")["duration_hours"].mean()
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    average = average.reindex(order).dropna()  # days that never happened are left out
    average.plot(kind="bar", rot=45)
    plt.title("Average recorded hours by day of the week")
    plt.ylabel("Average hours per day")
    save_and_show("weekday_average.png")


def chart_work_study(df):
    daily = analysis.work_study_per_day(df)
    plt.scatter(daily["Work"], daily["Study"])
    plt.title("Work and study hours per day")
    plt.xlabel("Work hours")
    plt.ylabel("Study hours")
    save_and_show("work_vs_study.png")


def chart_weekly(df):
    weekly = analysis.weekly_hours(df)
    weekly.plot(kind="bar", stacked=True, rot=0)
    plt.title("Recorded hours per week")
    plt.xlabel("Week starting on")
    plt.ylabel("Hours")
    plt.legend(bbox_to_anchor=(1, 1))  # put the legend outside of the bars
    save_and_show("hours_per_week.png")


CHARTS = [
    ("Hours per category", chart_categories),
    ("Hours for every day", chart_daily),
    ("Average hours by day", chart_weekday),
    ("Work and study per day", chart_work_study),
    ("Hours per week", chart_weekly),
]