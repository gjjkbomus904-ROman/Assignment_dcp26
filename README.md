# My Daily Time Spending

Proposal-stage project package prepared on 30 October 2026.

## Questions

1. Which categories have the greatest totals of recorded hours?
2. How do recorded work and study hours compare?
3. How do daily totals and categories vary between weekdays and weekends?

## Data Dictionary

One row represents one recorded activity entry. All fields are populated in the supplied file.

| Column | Type | Units / format | Description and measurement |
| --- | --- | --- | --- |
| `date` | Date | YYYY-MM-DD | Activity date as recorded by the user. Entry time is unknown. |
| `activity` | Categorical text | None | User's activity label, for example Working or University. |
| `category` | Categorical text | None | User's grouping: Work, Study, Leisure, Social, Sport, Trip or Meeting. |
| `duration_hours` | Number | Hours | User's recorded duration. Instrument, rounding and overlap rules are not supplied. |
| `notes` | Text | None | User's contextual description of the activity. |

See [Data_Dictionary.md](Data_Dictionary.md) for observed values and validation rules.

## Description of the project

I plan to analyse my recorded activities to understand my allocation of time. The current CSV has 23 entries on 12 consecutive dates, 19–30 October 2026, totalling 120 recorded hours. It contains five columns, including dates, a numeric duration and categorical labels. The data covers selected activities rather than full 24-hour days.

See [Proposal.md](Proposal.md) for the scope and development plan.

## Instructions for use

Open `data/time_spending.csv` in a text editor or CSV viewer to inspect the original records. Read the proposal and validation report alongside it. There is no executable application in this proposal package.

## How it works

Planned flow: CSV validation, SQLite storage, SQL and pandas analysis, matplotlib charts, then a text menu for choosing analyses and filters. Implementation is future work.

## Findings

The following are direct descriptive calculations from the supplied file, not results from a completed application.

| Category | Entries | Recorded hours |
| --- | ---: | ---: |
| Work | 6 | 53 |
| Social | 6 | 18 |
| Study | 5 | 16 |
| Meeting | 2 | 15 |
| Trip | 1 | 9 |
| Sport | 2 | 7 |
| Leisure | 1 | 2 |
| **Total** | **23** | **120** |

Work has the largest recorded total. Work exceeds Study by 37 recorded hours. Daily totals range from 6 to 14 hours. These figures cannot establish the distribution of all time spent: coverage is incomplete, overlapping activities cannot be ruled out, and the observation window is short.

## Data collection evidence and reflection

The file has entries for every date in its 12-day range, but it does not prove same-day collection. No collection photographs, diary, measurement method or GitHub history were supplied for verification. They have not been fabricated. The student should add genuine collection photographs and an account of the actual measurement process, including any rounding and overlapping activities.

Social and Meeting are similar concepts but remain separate as recorded. Trip and Competition on 24 October may need clarification about overlap. The small weekend sample limits comparisons. Future collection should document duration measurement and maintain consistent category definitions.

## List of files in the project

| File | Source / purpose |
| --- | --- |
| `data/time_spending.csv` | Original user-supplied data, copied byte for byte |
| `Proposal.md` | Project proposal drafted with AI assistance from the supplied data |
| `README.md` | Project documentation drafted with AI assistance |
| `Data_Dictionary.md` | Schema documentation drafted with AI assistance |
| `Validation_Report.md` | Checks and calculations on the supplied CSV |

## References

- [Assignment brief](https://github.com/skooter500/dcp26-assignment/blob/main/dataset_assignment.md)
- [Required README structure](https://github.com/skooter500/dcp26-assignment/blob/main/README.MD)

The brief lists a pass/fail proposal repository submission but gives no 30 October deadline. That date is the requested preparation target; the course submission system should be checked for the official deadline.

## What I am most proud of in the assignment

Student reflection has not yet been supplied. This section will be completed by the student as the project develops.

## What I learned

Student reflection has not yet been supplied. Current data review shows why category definitions, measurement rules and coverage matter when interpreting totals.

## AI assistance

AI checked the provided file and drafted documentation. No data records or measurement values were generated or changed. Personal reflections, photographs and collection evidence must come from the student.
