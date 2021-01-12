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

To remove `?`from page selector:

- Add page footer
- Add text box with Built-in Overall Total Page count
- To hide that text box:
  - Text box properties
  - Visibilites
    - Hide

To show/hide a column:

- Right click column header
- Column Visibility
  - Hide

To show/hide values based on value:

- IIF(expression, true-value, false-value)

  - expression = any boolean expression
  - true-value = the return value in the expression is TRUE
  - false-value = the return value in the expression is FALSE

- Add parameter

  - Available Values
    - add Yes/1, No/0
  - Default Values
    - add 1

- Show/hide row based on parameter
  - Select row
    - Row Visibility
    - Show or hide based on an expression
      - `IIF(expression, true-value, IIF(expression, true-value, false-value))`

## Implementing Filters

To implement filters:

- Tablix Properties
- Filters

| Static                       | Dynamic                    |
| ---------------------------- | -------------------------- |
| Predetermined filter         | Have options or conditions |
| Placed by the designer       | Allows the users to choose |
| Cannot be changed at runtime |                            |

Search Parameter filter:

- Parameters
  - Allow blank values
- Tablix Parameters
  - Filters
  - Search Parameters
  - Like

## Creating Dynamic Reports in SSRS Using Parameters

### Types of filters

| Dataset Filter                        | Report Filter                                                                        |
| ------------------------------------- | ------------------------------------------------------------------------------------ |
| Filter before teh dataset is returned | Filter after the dataset has been returned - available in the varilus levels of data |
| Can be bound to a parameter           | Can be bound to a report parameter                                                   |
| Optimal and preferred for performance |                                                                                      |

### Types of parameters

| Dataset Parameter                        | Report Parameter                                               |
| ---------------------------------------- | -------------------------------------------------------------- |
| Also called query parameter              | Contains the settings of the parameter                         |
| Perform a filter within the source query | Can be hidden, internal, or visible                            |
|                                          | Can be used to interact with the user                          |
|                                          | May be associated to a dataset parameter                       |
|                                          | Can be used in filtering, formatting, or visibility conditions |
|                                          | Can be associated to a dataset filter                          |

### Query Based vs Static Parameters

| Query Based Parameters               | Static Parameters                 |
| ------------------------------------ | --------------------------------- |
| Dynamic                              | Static                            |
| Gets the list of values from a query | Specified in teh Report Parameter |
