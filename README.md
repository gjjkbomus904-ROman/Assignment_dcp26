# My Daily Time Spending

Data Centric Programming Assignment 2026 – [Assignment Brief](https://github.com/skooter500/dcp26-assignment/blob/main/dataset_assignment.md)

# Questions

1. Where does my recorded time go: which categories take the largest share of the hours?
2. How different are Work and Study: in total hours and in the length of a typical session?
3. Do I work and study on the same days, or do they exclude each other?
4. Do my weeks look alike, or does the balance between Work and Study change from week to week?
5. How do weekends differ from weekdays: in the amount of recorded time and in what fills it?
6. Which days were the most and the least loaded, and what explains the extremes?

# Data Dictionary

One row = one activity I recorded by hand. A day can have several rows.
Data file: [`data/time_spending.csv`](data/time_spending.csv). More detail in [Data_Dictionary.md](Data_Dictionary.md).

| Column | Type | Units / format | How I record it |
| --- | --- | --- | --- |
| `date` | Date | YYYY-MM-DD | The day the activity happened |
| `activity` | Text (category label) | None | What I did, e.g. Working, University, Talking, Training |
| `category` | Text (categorical) | Work, Study, Social, Meeting, Sport, Trip, Leisure | My grouping of the activity |
| `duration_hours` | Number | Hours (whole numbers so far) | How long the activity took |
| `notes` | Text | None | Short description of the activity |

Rules: record the activity on the day it happens, one row per activity, durations in hours.
An activity can overlap with another one (for example a competition during a trip day), so a day can add up to more than the time I was actually awake for a single activity.

# Description of the project

A Python application that stores my hand-recorded time log in SQLite, analyses it with pandas, draws charts with matplotlib and lets me explore it through a text menu.

- **Dataset:** 33 rows, 20 consecutive days (2026-10-19 to 2026-11-07), 176 recorded hours, 5 columns.
- **Not a full diary:** it covers the main activities of the day, not every hour. A day without a Study row does not prove I did not study, it only means I did not record it.

## Data collection and diary

> **TODO (me):** add 2–3 photos of how I collect the data (notebook, phone notes…) in `images/` and link them here, e.g. `![notebook](images/notebook.jpg)`.
>
> **TODO (me):** describe how I really recorded the data (where, at what time of day, what I used to measure the duration, rounding) and explain gaps: the log stops on 2026-11-07, and several days were committed together (19–23 Oct on 24 Oct, 2–7 Nov on 8 Nov). I wrote down several days in a notebook and then added. Be honest about when entries were written.


On start the program rebuilds the database from `data/time_spending.csv`, checks every row and prints any problems. Menu:

```
=== My Time Tracker ===
1. Show entries (filter by category / dates)
2. Run a prepared SQL query
3. Analysis summary (pandas)
4. Make charts (saved to charts/)
5. Add an entry
0. Exit
```

"Add an entry" validates the input (real date, not in the future, number of hours between 0 and 24), appends the row to the CSV and the database. After adding, commit the CSV to GitHub.

# How it works:

| File | Role |
| --- | --- |
| `src/db.py` | Creates the SQLite table (with a `CHECK` on the duration), validates each CSV row (date, empty text, unknown category, duration range, duplicates, days over 24 h) and loads it. Bad rows are rejected with a reason, odd rows are only flagged. |
| `src/queries.py` | Six SQL queries using `GROUP BY`, `ORDER BY`, `WHERE`, `COUNT`, `SUM`, `AVG`. |
| `src/analysis.py` | pandas functions (category summary, weekday analysis, weekday vs weekend, work vs study, correlation) and six matplotlib charts. |
| `src/main.py` | The text menu. |

The CSV is the source of truth (it is what I record and commit). The database is rebuilt from it on every start, so the two never disagree.

# Findings

All numbers come from the program (menu options 2, 3 and 4) and match the current `data/time_spending.csv`: 33 rows, 20 days, 176 hours.

| Category | Entries | Hours | Share |
| --- | ---: | ---: | ---: |
| Work | 7 | 62 | 35% |
| Study | 9 | 35 | 20% |
| Meeting | 5 | 34 | 19% |
| Social | 8 | 27 | 15% |
| Trip | 1 | 9 | 5% |
| Sport | 2 | 7 | 4% |
| Leisure | 1 | 2 | 1% |


