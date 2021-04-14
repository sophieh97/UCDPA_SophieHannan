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

def pie(category):
    label = []
    label_percent = []
    for cat in data[category].unique():
        label.append(cat)
        t1 = data[(data[category] == cat) & (data['Attrition'] == 'Yes')].shape[0]
        t2 = data[data[category] == cat].shape[0]
        label_percent.append(t1/t2 * 100)
    fig1, ax1 = plt.subplots()
    ax1.pie(label_percent, labels=label, autopct='%1.1f%%', shadow=True, startangle=180)
    centre_circle = plt.Circle((0,0),0.75,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')
    plt.title(category)
    plt.show()

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
my_dict_general_data1 = dict({1: "Below College", 2: "College", 3: "Bachelor", 4: "Master", 5: "Doctor"})
data["Education"] = data["Education"].replace(my_dict_general_data1)
print(data.head())
data.rename(columns={"Education": "EducationLevel"}, inplace=True)
value_counts(["DistanceFromHome","Attrition"])
value_counts(["Department", "Attrition"])
value_counts(["BusinessTravel", "Attrition"])
value_counts(["NumCompaniesWorked", "Attrition"])
print(data.iloc[:12, :12])
loop(data)
general_data = data
general_data = set_index("EmployeeID")
# Final check before merge
print(general_data.isnull().sum())


# Merge DataFrames
df1 = pd.merge(employee_survey_data, general_data, how="inner", on="EmployeeID")
data = pd.merge(manager_survey_data, df1, how="inner", on="EmployeeID")
# Code check complete
data = set_index("EmployeeID")
print(data.columns)
print(data.iloc[:13, :13])
print(data.isnull().sum())

# Numpy on merged dataframes
arr = data.to_numpy()
columns = ['EmployeeID', 'JobInvolvement', 'PerformanceRating',
       'EnvironmentSatisfaction', 'JobSatisfaction', 'WorkLifeBalance', 'Age',
       'Attrition', 'BusinessTravel', 'Department', 'DistanceFromHome',
       'EducationLevel', 'EducationField', 'Gender', 'JobLevel', 'JobRole',
       'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike',
       'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
       'YearsAtCompany', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
dataframe = print('\nNumpy Array Datatype :', arr, columns)
np_dataframe = np.array(dataframe)
print(type(np_dataframe))

# Matplotlib and Seaborn Graphs
# Attrition by Gender
sns.set_style("whitegrid")
sns.set_palette("muted")
fig, ax = plt.subplots()
sns.countplot(x = "Attrition",data=data,hue="Gender")
ax.set(title="Attrition by Gender")
plt.show()
plt.close()

plt.figure(figsize=(8,8))
ax = sns.countplot(x='Attrition', data=data, hue="Gender")
ax.set_ylabel('# of Employee')
ax.set(title="Attrition by Gender")
bars = ax.patches
half = int(len(bars)/2)
left_bars = bars[:half]
right_bars = bars[half:]

for left, right in zip(left_bars, right_bars):
    height_l = left.get_height()
    height_r = right.get_height()
    total = height_l + height_r

    ax.text(left.get_x() + left.get_width()/2., height_l + 40, '{0:.0%}'.format(height_l/total), ha="center")
    ax.text(right.get_x() + right.get_width()/2., height_r + 40, '{0:.0%}'.format(height_r/total), ha="center")


# Attrition by Age
fig, ax = plt.subplots()
sns.violinplot(y='Age',x='Attrition',data=data)
ax.set(title="Attrition by Age")
plt.show()
plt.close()

# Attrition by Demographics
fig, ax = plt.subplots()
sns.set_palette("Set2")
demographics = sns.catplot(x="Gender",
                y="Age", data=data,
                kind="box", hue="Attrition")
demographics.fig.suptitle("Attrition by Demographics")
plt.show()


# Attrition by Business Travel
fig, ax = plt.subplots()
Business_Travel = sns.countplot(x = "Attrition",data=data,hue="BusinessTravel")
Business_Travel= ax.set(title="Attrition by Business Travel")
plt.show()
plt.close()

# % of Attrition by Business Travel
pie('BusinessTravel')

# Attrition by Department
fig, ax = plt.subplots()
Business_Travel = sns.countplot(x = "Attrition",data=data,hue="Department")
Business_Travel= ax.set(title="Attrition by Department")
plt.show()
plt.close()

# % of Attrition by Department
pie("Department")

# Attrition by Education Level
fig, ax = plt.subplots()
Business_Travel = sns.countplot(x = "Attrition",data=data,hue="EducationLevel")
Business_Travel= ax.set(title="Attrition by Education Level")
plt.show()
plt.close()

# % of Attrition by Education Level
pie("EducationLevel")

# Attrition by Education field
fig, ax = plt.subplots()
Business_Travel = sns.countplot(x = "Attrition",data=data,hue="EducationField")
Business_Travel= ax.set(title="Attrition by Education Field")
plt.show()
plt.close()

# % of Attrition per Job Role
pie("JobRole")























