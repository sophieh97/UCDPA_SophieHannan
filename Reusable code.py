import pandas as pd

#Importing and Inital Review of Data: employee_survey
def import_data(filename):
    data = pd.read_csv(filename)
    print(data)
    print(data.head())
    print(data.info())
    print(data.describe())
    print(data.shape)
    print(data.columns)
    print(data.index)
    return data

data = import_data("XYZ Company/employee_survey_data.csv")

#Analysing Data: employee_survey
#Sorting employee_survey from lowest to highest
def sort_values (columns):
    employee_survey_dataset = data.sort_values(columns)
    print(employee_survey_dataset.head())
    print(employee_survey_dataset.info)

employee_survey_dataset = sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])

#Importing and Inital Review of Data: manager_survey
data = import_data("XYZ Company/manager_survey_data.csv")

#Analysing Data: manager survey
#Sorting manager survey from lowest to highest
employee_survey_dataset = sort_values(["JobInvolvement", "PerformanceRating"])

#Importing and Inital Review of Data: general_data
data = import_data("XYZ Company/general_data.csv")

# Analysing Data: manager survey
def groupby(column):
    manager_survey_dataset = data.groupby(column)
    print(manager_survey_dataset.head())

#find out how to reorder dataframe **
#Change the Order of Dataframe: - reorder dataframe
manager_survey_dataset = data.set_index("EmployeeID").sort_index()
manager_survey_data = groupby("Department")
print(manager_survey_dataset.head())






