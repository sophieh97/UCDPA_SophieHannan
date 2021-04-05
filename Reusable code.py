import pandas as pd

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
data = import_data("XYZ Company/general_data.csv")
data = import_data("XYZ Company/in_time.csv")
data = import_data("XYZ Company/manager_survey_data.csv")
data = import_data("XYZ Company/out_time.csv")

