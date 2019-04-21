"""
using_functions.py contains a function that checks to see if a given
dataframe matches the City of Seattle Wage Data:
-- column names
-- column data types
-- and contains at least 10 rows in the test data frame
"""

import pandas as pd

# import City of Seattle Wage Data
wages = pd.read_csv('https://data.seattle.gov/api/views/2khk-5ukd/rows.csv?'
                    'accessType=DOWNLOAD', sep=',', header=0)


def test_create_dataframe(df):
    """
    Inputs: a pandas dataframe df
    Ouputs: returns true only if the following are all true
    - df contains only the columns in wages
    - the columns contain the correct data type
    - there are at least 10 rowns in df
    """
    if (df.shape[0] >= 10 and
        list(wages) == list(df) and
            wages.dtypes.equals(df.dtypes)):
        return True
    else:
        return False
