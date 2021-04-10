import pandas as pd


# Importing and Inital Review of Data: employee_survey
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


# Analysing Data: employee_survey
# Sorting employee_survey from lowest to highest
def sort_values(columns):
    employee_survey_dataset = data.sort_values(columns)
    print(employee_survey_dataset.head())


sort_values(["EnvironmentSatisfaction", "JobSatisfaction", "WorkLifeBalance"])

# Importing and Inital Review of Data: manager_survey
data = import_data("XYZ Company/manager_survey_data.csv")

# Analysing Data: manager survey
# Sorting manager survey from lowest to highest
sort_values(["JobInvolvement", "PerformanceRating"])

# Importing and Inital Review of Data: general_data
data = import_data("XYZ Company/general_data.csv")

# Subsetting by row/column number
def iloc(row,column):
    iloc = print(data.iloc[row,column])
    print(iloc)
    return data

#The below works - tried making it better on other page to use again for If statements and Numpy
data["JobInvolvement"] = data["JobInvolvement"].replace({1: "Low", 2: "Medium", 3: "High", 4: "Very High"})
data["PerformanceRating"] = data["PerformanceRating"].replace({1: "Low", 2: "Good", 3: "Excellent", 4: "Outstanding"})

# Merge Data Code when fixed - add when FIXED
df1 = pd.merge(employee_survey_data, general_data, how="inner", on="EmployeeID")
data = pd.merge(manager_survey_data, general_data, how="inner", on="EmployeeID")

my_dict_general_data = dict({1: "Below College", 2: "College", 3: "Bachelor", 4: "Master", 5: "Doctor"})
data["Education_Level"] = data["Education_Level"].replace(my_dict_general_data)
print(data.head())


# need to create a list to do it
BusinessTravel = ("Non-Travel", "Travel_Rarely", "Travel_Frequently")
Attrition = ("Yes", "No")
np_BusinessTravel = np.array("BusinessTravel")
np_Attrition = np.array("Attrition")
np_travel_attrition = np_BusinessTravel[np_Attrition == 'Yes']
print(np_Attrition)


