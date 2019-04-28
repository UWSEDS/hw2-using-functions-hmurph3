# HW2 - Using Functions

##### Grade: 2/7

-3: Didn't check that the dataframe has at least 3 columns.
-1: Didn't check that  the dataframe contains only the columns that you specified in #1.
-1: When checking if the columns contain the correct data types, your test implicitly depended on the order of the columns (even though your dataframe only had 1 column, this is still suboptimal).

-----


Create a python module (a file with extension ‘.py’) with the following functions:

1. (4 points) Find an on-line data source (e.g., from data.gov). Write python codes that read the on-line file and create a data frame that has at least 3 columns.

1. (3 points) Create the function test_create_dataframe that takes a pandas DataFrame as input and returns True if the following conditions hold:

   1. The DataFrame contains only the columns that you specified in #1.
   1. The columns contain the correct data type
   1. There are at least 10 rows in the DataFrame.

The data source I used for this is the City of Seattle Wage Data that can be found at https://data.seattle.gov/City-Business/City-of-Seattle-Wage-Data/2khk-5ukd.
