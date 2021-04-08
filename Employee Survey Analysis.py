import pandas as pd


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


# Counting Data
def value_counts(columns):
    value_counts = data[columns].value_counts()
    print(value_counts.isnull().sum())
    print(value_counts.head())
    return data


data = import_data("XYZ Company/employee_survey_data.csv")
clean_data(data)
sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
my_dict(["EnvironmentSatisfaction","JobSatisfaction", "WorkLifeBalance"])
value_counts("EnvironmentSatisfaction")
value_counts("JobSatisfaction")
value_counts("WorkLifeBalance")
#check if employee ID still in it if not do separtely like below

# Manager Survey Analysis
data = import_data("XYZ Company/manager_survey_data.csv")
data ["JobInvolvement"] = data["JobInvolvement"].replace({1:"Low", 2:"Medium", 3:"High", 4:"Very High"})
data ["PerformanceRating"] = data["PerformanceRating"].replace({1:"Low", 2:"Good", 3:"Excellent", 4:"Outstanding"})
print(data.head())
value_counts("JobInvolvement")
value_counts("PerformanceRating")

# In Time
