"""
using_functions.py contains a function that checks to see if a given
dataframe matches the City of Seattle Wage Data:
-- column names
-- column data types
-- and contains at least 10 rows in the test data frame

The City of Seattle Wage Data has the following information
There are 5 columns and 12.1K rows.
The columns and their data types are listed below.
Department: String
Last Name: String
First Name: String
Job Title: String
Hourly Rate: Float
"""

import pandas as pd

# import City of Seattle Wage Data
URL = 'https://data.seattle.gov/api/views/2khk-5ukd/rows.csv?accessType=DOWNLOAD'
DATA = pd.read_csv(URL, sep=',', header=0)

# get the column names and column datatypes
COL_NAMES = sorted(DATA.columns)
COL_TYPES = list(DATA[COL_NAMES].dtypes)

def test_create_dataframe(dataframe):
    """
    Inputs: a pandas dataframe df
    Ouputs: returns a Boolean.

    The function checks if the dataframe column names and data types
    match the City of Seattle Wage Data and there are at least 10 rows
    and at least 3 columns
    """

    test_passed = True
    col_count = dataframe.shape[1]
    row_count = dataframe.shape[0]
    column_names = sorted(dataframe.columns)
    column_types = list(dataframe[column_names].dtypes)

    # Check that there are at least 3 columns
    if col_count < 3:
        test_passed = False
    # Check that there are only the columns defined in COL_NAMES
    elif column_names != COL_NAMES:
        test_passed = False
    # Check that there the datatypes match COL_TYPES
    elif column_types != COL_TYPES:
        test_passed = False
    # Check that there are more than 10 Columns
    elif row_count < 10:
        test_passed = False

    return test_passed
