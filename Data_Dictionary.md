# Data Dictionary: My Daily Time Spending

Source: [`data/time_spending.csv`](data/time_spending.csv), recorded by hand. 33 rows on 20 consecutive days (2026-10-19 to 2026-11-07), 176 recorded hours. One row is one recorded activity. A day can have several rows.

## CSV columns

| Column | Type | Units / format | Observed values | How it is recorded and validated |
| --- | --- | --- | --- | --- |
| `date` | Date | `YYYY-MM-DD` | 2026-10-19 to 2026-11-07, every day in the range has at least one row | The day the activity happened. Must be a valid date and not in the future. |
| `activity` | Text | None | University, Test preparation, Gaming, Talking, Working, Training, Competition, Trip with teammates, Meeting | What I did, in my own words. Must not be empty. |
| `category` | Categorical text | One of: Work, Study, Social, Meeting, Sport, Trip, Leisure | Work 7 rows, Study 9, Meeting 5, Social 8, Trip 1, Sport 2, Leisure 1 | My grouping of the activity. Must not be empty. Any other label is flagged as a warning. |
| `duration_hours` | Number | Hours | Whole numbers from 2 to 10 so far | How long the activity took. Must be a number greater than 0 and at most 24. |
| `notes` | Text | None | Short descriptions, e.g. "Worked at my job", "Handball training" | Optional. An empty note is stored as NULL in the database. |

## Database table `activities` (SQLite)

Built from the CSV by `src/db.py` every time the program starts.

| Column | SQLite type | Constraint |
| --- | --- | --- |
| `id` | INTEGER | Primary key, added automatically (not in the CSV) |
| `date` | TEXT | NOT NULL, ISO format |
| `activity` | TEXT | NOT NULL |
| `category` | TEXT | NOT NULL |
| `duration_hours` | REAL | NOT NULL, `CHECK (duration_hours > 0 AND duration_hours <= 24)` |
| `notes` | TEXT | May be NULL |

## Derived columns (not recorded, calculated in pandas)

| Column | Meaning |
| --- | --- |
| `weekday` | Day name calculated from `date` |
| `is_weekend` | True for Saturday and Sunday |

## Validation when loading

- Rejected (row is not loaded, reason is printed): invalid or future date, empty activity or category, duration that is not a number or outside (0, 24].
- Flagged only (row is loaded, a warning is printed): a category outside the list above, an exact duplicate row, a day with more than 24 recorded hours.
- Current result: 33 rows loaded, 0 rejected, 0 warnings.

## Interpretation rules

- No column is a unique record identifier in the CSV, so exact duplicates are flagged and not deleted automatically: two identical entries could be genuine.
- A day without a row for some category means it was not recorded. It does not prove that zero time was spent on it.
- The log is not a complete account of every hour of a day: it has no start or end times and no sleep.
- Activities can overlap. For example on 2026-10-24 a Competition (5 h) and a Trip (9 h) were recorded on the same day, giving 14 h.
- Social and Meeting are kept as two separate categories, as I recorded them.
- Durations are whole hours, so differences smaller than an hour cannot be seen.
- How and when each entry was written down is described in the diary section of the [README](README.md).
