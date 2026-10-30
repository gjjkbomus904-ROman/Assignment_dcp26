# Proposal: My Daily Time Spending

Prepared for the proposal stage on 30 October 2026.

## Project description and aim

This project will explore how my recorded time is distributed between work, study, sport, leisure, social activities, meetings and trips. The aim is to understand which recorded activities take the most time and how the recorded totals vary by date and day of the week.

The supplied CSV contains 23 activity records across 12 consecutive dates, from 19 to 30 October 2026. Its five columns are `date`, `activity`, `category`, `duration_hours` and `notes`. Each row represents one recorded activity entry. The file contains 120 recorded hours. It is a partial activity log, not a complete account of every hour in each day.

## Research questions

1. Which categories account for the largest totals of recorded hours?
2. How do recorded work hours compare with recorded study hours over the observed period?
3. How do daily recorded totals and category totals differ across weekdays and weekends?

The third question is exploratory: the current sample includes only one Saturday and one Sunday. Missing activity entries cannot be interpreted as evidence that an activity did not happen.

## Data and measurement

The original user-supplied CSV is preserved in `data/time_spending.csv` without changing its bytes or adding records. See the data dictionary in `README.md` and `Data_Dictionary.md` for the observed schema and values.

The CSV does not state the original measurement instrument, rounding rule, collection time or whether activities overlap. These details remain unverified. For ongoing collection, the proposed method is to record actual activities on the day, note their duration using observed start and end times or a timer, and record any rounding and overlap explicitly. This proposed method is not a claim about how the existing entries were collected.

## Planned application

The final application will use Python to validate the CSV and load it into SQLite. SQL queries and pandas will calculate category totals, work/study comparisons and daily summaries. Matplotlib charts will show category totals and recorded hours over time. A text menu will let a user select these analyses and filter by date or category. Weekday labels will be derived from dates during analysis rather than added as invented observations.

## Current status and next steps

The current package contains the proposal, documentation, original data and a validation report. The application is planned and has not been implemented. Continue genuine daily collection and commits, retain collection evidence and document measurement rules. Do not reconstruct a past collection or commit history. The supplied CSV alone cannot establish when its entries were recorded.

## References and assistance

AI assistance was used to check the supplied CSV and draft this documentation. No dataset values were generated, replaced or inferred. The student should review the wording and be able to explain the project.
