#https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset
#https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study?select=employee_survey_data.csv - This one very good!!

#analyse two companies data to uncover what factors are contributing to employee attrition and try to prediction turnover for both
#look at data before decision
#any commonalities
#make sure aloy of values
#one database multiple merges need

data = import_data("XYZ Company/general_data.csv")
data = import_data("XYZ Company/in_time.csv")
data = import_data("XYZ Company/manager_survey_data.csv")
data = import_data("XYZ Company/out_time.csv")

manager_survey_dataset = sort_values(["EmployeeID"])

# Select the state and family_members columns
state_fam = homelessness[["state", "family_members"]]
# Print the head of the result
print(state_fam.head())
manager_survey_dataset = data.set_index("EmployeeID").sort_index()
#use this to reorder DF
store_counts = store_types["type"].value_counts()
print(store_counts)
# Analysing Data: manager survey
def groupby():
    manager_survey_dataset = data.groupby(column)[column].sum
    print(manager_survey_dataset.head())
manager_survey_dataset = data.groupby("Department")["Attrition"].sum()


# Analysing Data: manager survey
def groupby(column):
    manager_survey_dataset = data.groupby(column)
    print(manager_survey_dataset.head())

#find out how to reorder dataframe **
#Change the Order of Dataframe: - reorder dataframe
manager_survey_dataset = data.set_index("EmployeeID").sort_index()
manager_survey_data = groupby("Department")
print(manager_survey_dataset.head())
# Change the Order of Dataframe:
manager_survey_dataset = data.groupby("Department")["Attrition"].sum()
