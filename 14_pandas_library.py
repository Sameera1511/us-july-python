# Pandas:
    # Pandas is a python library usedfor working with data sets.
    # Pandas has functions for analyzing, cleaning, exploring and manipulating data.

    # Python Data Analysis => Pandas

    # It allows you to analyze data

# What pandas can do ?
    # Correlations between two or more columns
    # Aggregation


import pandas as pd

# mydataset = {
#     "cars": ["BMW", "volvo", "ford"],
#     "passings": [3, 7, 2]
# }

# df = pd.DataFrame(mydataset)

# print(df)
#--------------------------------
# age = [23, 34, 45, 56]

# s1 = pd.Series(age)
# print(s1)
#-------------------------------

# print(pd.__version__)

# Series:
    # Pandas Series is just like a column
    # It is also one-diamensional array holding any type of data

# names = ("Arjun", "Dev", "Jay")
# name_s1 = pd.Series(names, index=["x", "y", "z"])   # x, y, x are labels

# print(name_s1["x"])

# print(name_s1[0])
# print(name_s1[2])
# # print(name_s1)


#---------------------------
# calories ={
#     "day1": 420,
#     "day2": 380, 
#     "day3": 390
# }

# my_cal = pd.Series(calories)
# print(my_cal)

#------------

# hr_spreadsheet = {
#     "empID": [101, 102, 103, 104, 105, 106],
#     "firstName": ["Karuna", "Daya", "Prem", "Shanti", "Bhavana", "Priya"],
#     "lastName": ["Patel", "Rathi", "Chopra", "Shaw", "Lambani", "Jadhav"],
#     "Age": [34, 32, 29, 30, 35, 33],
#     "Salary": [45000, 56300, 40000, 35900, 50200, 48000] 
# }


# df_hr_spreadsheet = pd.DataFrame(hr_spreadsheet)
# print(df_hr_spreadsheet)
