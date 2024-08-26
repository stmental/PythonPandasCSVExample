# PythonPandasCSVExample

Small Python script to load a CSV file into a Panda DataFrame, do some processing and then output to a new CSV file

The input file consists of 2 columns:
- patient_id: string that identifies a patient
- month_year: string identifying a month an year that a patient began or ended enrollment

## Assumptions
- There is always an even number of rows per patient ID.  While a signle patient may have multiple enrollment spans, there will never be a start date without an end date.

## Processing
Create a span table for each patient ID.  Essentially calculate all the span(s) for each patient and output them.  Only one span per output row, so a patient may have multiple rows if they have multiple spans

## Files
- pandas_test.py - This is the python script
- test_data.csv - Example file that the script uses
- Pipfile - Defines the python version and required libraries for script.  Use [pipenv](https://pypi.org/project/pipenv) to install these dependencies.
