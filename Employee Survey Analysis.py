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
    rename = data.rename(columns={column: "EducationLevel"}, inplace=True)
    print(data.columns)
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
    value_counts = data[columns].value_counts(ascending=False)
    print(value_counts)
    return data


# Need to remove isnull here when fixed

# Employee Survey Data
data = import_data("XYZ Company/employee_survey_data.csv")
clean_data(data)
set_index("EmployeeID")
sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
my_dict(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
# Dont think these work
value_counts("EnvironmentSatisfaction")
value_counts("JobSatisfaction")
value_counts("WorkLifeBalance")
loop(data)
employee_survey_data = data
print(employee_survey_data.head())

# Check if employee ID still in it if not do separtely like below - think will have to do separte

# Manager Survey Analysis
data = import_data("XYZ Company/manager_survey_data.csv")
set_index("EmployeeID")
my_dict_manager_survey1 = dict({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
data["JobInvolvement"] = data["JobInvolvement"].replace(my_dict_manager_survey1)
print(data.head())
my_dict_manager_survey2 = dict({1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"})
data["PerformanceRating"] = data["PerformanceRating"].replace(my_dict_manager_survey2)
print(data.head())
#Dont think these work correctly
value_counts("JobInvolvement")
value_counts("PerformanceRating")
loop(data)
manager_survey_data = data
print(manager_survey_data.head())

# General data
data = import_data("XYZ Company/general_data.csv")
clean_data(data)
set_index("EmployeeID")
# kept martial status from drop
data_drop(["EmployeeCount", "StandardHours", "Over18"])
rename("Education")
# Can only do values not numbers
value_counts(["Department", "Attrition"])
value_counts(["BusinessTravel", "Attrition"])
value_counts(["MaritalStatus", "Attrition"])
value_counts(["NumCompaniesWorked", "Attrition"])
print(data.iloc[:5, :5])
loop(data)
general_data = data
print(general_data.head())















