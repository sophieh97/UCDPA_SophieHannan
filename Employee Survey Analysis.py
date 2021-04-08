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
def cleandata(data):
    data = data.fillna("null")
    print(data.isnull().sum())
    print(data.head())
    print(data.shape)
    return (data)

# Sorting employee_survey from lowest to highest
def sort_values(columns):
    employee_survey_replace = data(column).replace({1:"Low", 2:"Good", 3:"Excellent", 4:"Outstanding"})
    employee_survey_data = data.sort_values(columns)
    print(employee_survey_data.head())
    print(employee_survey_data.shape)
    return(data)

# Counting Data
def value_counts(columns):
    employee_survey_dataset = data[columns].value_counts()
    print(data.isnull().sum())
    print(employee_survey_dataset.head())
    return(data)

data = import_data("XYZ Company/employee_survey_data.csv")
cleandata(data)
sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])
value_counts("EnvironmentSatisfaction")
value_counts("JobSatisfaction")
value_counts("WorkLifeBalance")

