# Data Dictionary: My Daily Time Spending

Source: `data/time_spending.csv`, copied unchanged from the user-supplied `time_spending(3).csv`. One row is one recorded activity entry. Multiple entries can share a date.

| Column | Logical type | Units / format | Meaning and observed values | Measurement status and validation |
| --- | --- | --- | --- | --- |
| `date` | Date | `YYYY-MM-DD` | Calendar date associated with the activity; 2026-10-19 to 2026-10-30 | Recorded in source; require a valid date. Original entry time is unknown. |
| `activity` | Categorical text | None | Activity label: University, Test preparation, Gaming, Talking, Working, Training, Competition, Trip with teammates, Meeting | Preserve the user's label; require nonempty text. Labels alone do not establish timing or overlap. |
| `category` | Categorical text | None | Study, Leisure, Social, Work, Sport, Trip, Meeting | Preserve exact labels and case. Social and Meeting are distinct in the source; do not merge silently. |
| `duration_hours` | Number | Hours | Recorded duration of the activity entry; observed values are whole numbers from 2 to 10 | Actual instrument and rounding are unspecified. Require a finite positive number; flag values over 24 for review. Decimal hours can be supported in future collection. |
| `notes` | Text | None | Context supplied for the activity, such as test preparation or handball training | All current entries have notes. Preserve original wording; do not infer missing measurements from notes. |

## Interpretation rules

- No column is a unique record identifier. Exact duplicate rows should be flagged for review, not automatically deleted.
- A day without a category entry means it was not recorded; it does not prove zero time was spent on that category.
- The file does not contain start/end times, sleep or complete daily coverage. Do not fill the remainder of a day or assume activities cannot overlap.
- Any future category mapping or correction should be documented separately from the original source.
- Day of week may be calculated from `date`; it is not an original CSV column.

These definitions document the existing file. They do not establish that measurement rules were agreed before collection. Historical collection details require the student's own evidence.
