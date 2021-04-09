import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Importing and Review of Data: employee_survey
def import_data(filename):
    data = pd.read_csv(filename)
    print(data)
    print(data.head())
    print(data.info())
    print(data.isnull().sum())
    print(data.describe())
    print(data.shape)
    print(data.columns)
    print(data.index)
    return data


# Analysing data
# Missing Values
def clean_data(data):
    data = data.fillna("null")
    print(data.isnull().sum())
    print(data.head())
    print(data.shape)
    return data


# Rename Columns
def rename(column):
    rename = data.rename({column: "EmployeeID"}, axis=1, inplace=False)
    print(rename.shape())
    return data


# Drop Columns
def data_drop(columns):
    data_drop = data.drop((columns), axis=1, inplace=True)
    print(data.shape)
    return data


# Set Index
def set_index(column):
    set_index = data.set_index(column)
    print(set_index.head())
    return data


# Sorting employee_survey from lowest to highest
def sort_values(columns):
    sort_values = data.sort_values(columns)
    print(sort_values.head())
    print(sort_values.shape)
    return data


# Replace using a dictionary
def my_dict(columns):
    my_dict = data[columns].replace({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
    print(my_dict.head())
    print(data.head())
    return data

# Looping Iterrows
def loop(data):
    for lab, row in data.iterrows():
        print(lab)
        print(row)
    return data


# Counting Data
def value_counts(columns):
    value_counts = data[columns].value_counts()
    print(value_counts.isnull().sum())
    print(value_counts.head())
    return data


# Need to remove isnull here when fixed

# Employee Survey Data
data = import_data("XYZ Company/employee_survey_data.csv")
clean_data(data)
set_index("EmployeeID")
sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
my_dict(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
value_counts("EnvironmentSatisfaction")
value_counts("JobSatisfaction")
value_counts("WorkLifeBalance")
loop(data)
# Check if employee ID still in it if not do separtely like below - think will have to do separte

# Manager Survey Analysis
data = import_data("XYZ Company/manager_survey_data.csv")
set_index("EmployeeID")
data["JobInvolvement"] = data["JobInvolvement"].replace({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
data["PerformanceRating"] = data["PerformanceRating"].replace({1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"})
print(data.head())
value_counts("JobInvolvement")
value_counts("PerformanceRating")
loop(data)

# General data
data = import_data("XYZ Company/general_data.csv")
clean_data(data)
set_index("EmployeeID")
data_drop("EmployeeCount")
data_drop("StandardHours")
data_drop("Over18")
data_drop("MaritalStatus")
value_counts("Department")
value_counts("Attrition")
loop(data)

