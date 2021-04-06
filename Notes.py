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

#use this to reorder DF


