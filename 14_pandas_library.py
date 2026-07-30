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

#----------------------

import pandas as pd

# df = pd.read_csv('./my_files/employees.csv')

# # print(df)
# print(df.to_string())

# print(pd.options.display.max_rows)
# pd.options.display.max_rows = 1000  # To change default display rows capacity
# print(pd.options.display.max_rows)  # To know systems rows display capacity


#------------------------

# df = pd.read_json("./my_files/healthcare.json")
# print(df)
# print(df.to_string())  # to_string() returns entire dataFrame

#----------------------------

# df = pd.read_excel("./my_files/ecommerce.xlsx")
# print(df)


#------------------------------------------
# Analyze DataFrame.

df = pd.read_csv("./my_files/employees.csv")
# print(df.head())  # Initial records
# print(df.tail(2))
# print(df.info())

#----------------------------
# Clean Data 

# Bad data:
    # Empty Cell
    # Wrong Data type
    # Wrong Data
    # Duplicates

# print(df)

# Cleaning Empty Cells:

 # Remove Rows:

# new_df = df.dropna()
# print(new_df)

# employees.csv => df => new_df
# df.dropna(inplace=True)
# print(df)

# Fill empty cells

# new_df = df.fillna(500)
# print(new_df)

# new_df = df.fillna({"age": 30, "salary": 50000})
# print(new_df)

#-------------------

# Get the mean of "age"
mean_age = df["age"].mean()
# print(mean_age)

# median_age = df["age"].median()
# print(median_age)

# mode_age = df["age"].mode()
# print(mode_age)

df.fillna({"age": mean_age}, inplace=True)
# print(df)

# mean_salary = df["salary"].mean()
# print(mean_salary)

# median_salary = df["salary"].median()
# print(median_salary)

mode_salary = df["salary"].mode()[1]
print(mode_salary)


# df.fillna({"salary": median_salary}, inplace=True)
# print(df)

df.fillna({"salary": mode_salary}, inplace=True)
# print(df)

#---------------------------

df["dob"] = pd.to_datetime(df["dob"], format='mixed')
df["dob"] = df["dob"].dt.strftime("%m/%d/%Y")
# print(df)


#---------------------------------------

df.loc[0, "salary"] = 55000
# print(df)

#-----------------------

for index in df.index:
    if df.loc[index, "Duration"] < 500:
        df.loc[index, "Duration"] = 700

print(df)
