"""
using_functions.py contains a function that checks to see if a given
dataframe matches the City of Seattle Wage Data:
-- column names
-- column data types
-- and contains at least 10 rows in the test data frame
"""

import pandas as pd

# import City of Seattle Wage Data
def create_data_frame():
    """
    Creates a dataframe from the City of Seattle Wage Data
    Returns the dataframe if there are more than three columns otherwise
    it returns "Dataframe as less than three columns"
    """
    wages = pd.read_csv('https://data.seattle.gov/api/views/2khk-5ukd/'
                        'rows.csv?accessType=DOWNLOAD', sep=',', header=0,
                        names=("Department", "LastName", "FirstName",
                               "JobTitle", "HourlyRate"),
                        dtype={"Department": str, "LastName": str,
                               "FirstName": str, "JobTitle": str,
                               "HourlyRate": float})
    if wages.shape[1] > 3:
        return wages
    else:
        raise ValueError("Unexpected column titles")


def test_create_dataframe(df):
    """
    Inputs: a pandas dataframe df
    Ouputs: returns true only if the following are all true
    - df contains only the columns in wages
    - the columns contain the correct data type
    - there are at least 10 rowns in df
    """
    column_titles = ["Department", "LastName", "FirstName", "JobTitle",
                     "HourlyRate"]

    if (all([title in df.columns for title in column_titles]) and
            list(column_titles.columns) == list(df.columns) and
            df.shape[0] > 10 and data.dtypes.Department == str and
            df.dtypes.LastName == str and df.dtypes.FirstName == str and
            df.dtypes.JobTitle == str and df.dtypes.HourlyRate == float):
        return True

