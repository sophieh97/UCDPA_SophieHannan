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
    my_dict_employee_survey = dict({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
    data[columns] = data[columns].replace(my_dict_employee_survey)
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

# Employee Survey Data - added data = to first few waiting shubham
data = import_data("XYZ Company/employee_survey_data.csv")
data = clean_data(data)
data = sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
value_counts("EnvironmentSatisfaction")
value_counts("JobSatisfaction")
value_counts("WorkLifeBalance")
loop(data)
employee_survey_data = data
employee_survey_data = my_dict(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
employee_survey_data = set_index("EmployeeID")
# Final check before merge
print(employee_survey_data.isnull().sum())


# Manager Survey Analysis
data = import_data("XYZ Company/manager_survey_data.csv")
data = sort_values(["JobInvolvement", "PerformanceRating"])
my_dict_manager_survey1 = dict({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
data["JobInvolvement"] = data["JobInvolvement"].replace(my_dict_manager_survey1)
print(data.head())
my_dict_manager_survey2 = dict({1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"})
data["PerformanceRating"] = data["PerformanceRating"].replace(my_dict_manager_survey2)
print(data.head())
value_counts("JobInvolvement")
value_counts("PerformanceRating")
loop(data)
manager_survey_data = data
manager_survey_data = set_index("EmployeeID")
# Final check before merge
print(manager_survey_data.isnull().sum())


# General data
data = import_data("XYZ Company/general_data.csv")
data = clean_data(data)
data = data_drop(["EmployeeCount", "StandardHours", "Over18", "MaritalStatus"])
data.rename(columns={"Education": "EducationLevel"}, inplace=True)
value_counts(["Department", "Attrition"])
value_counts(["BusinessTravel", "Attrition"])
value_counts(["NumCompaniesWorked", "Attrition"])
print(data.iloc[:5, :5])
loop(data)
general_data = data
general_data = set_index("EmployeeID")
# Final check before merge
print(general_data.isnull().sum())














