# Building Interactive SSRS

[Alexandra Santiago on Pluralsight](https://app.pluralsight.com/library/courses/ssrs-building-interactive-reports/exercise-files)

## Implementing Fixed Headers

To allow users to view headers in all pages of a table report:

- Row/Column Groups
  - Advanced Mode
  - Select first `(Static)` under Row Groups
  - Change Other Properties
    - KeepTogether = True
    - KeepWithGroup = After
    - RepeatOnNewPage = True
- To keep headers when scrolling:
  - FixedData = True

To allow users to view headers in all pages of matrix report:

- Tablix Properties
  - Row Headers
    - Repeat header rows on each page
  - Column Headers
    - Repeat header columns on each page
    - Keep header visible while scrolling

## Implementing Interactive Sorting

To implement interactive sorting:

- Need to specify what to sort, what to sort by, and the scope to which to apply the sort
- Static Sorting
  - Design
    - Tablix Properties
    - Sorting
    - Add sort by field
      - This will immediately sort fields
- Interactive Sorting
  - For each column to set up interactive sorting:
    - Column in Header row
    - Text Box Properties
    - Interactive Sorting
      - Enable
      - Sort by
      - Apply sorting to all groups in data set

Use ID fields to sort in the background

## Implementing Show/Hide Property
