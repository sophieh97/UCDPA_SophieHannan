import pandas as pd

def import_data(filename):
    data = pd.read_csv("XYZ Company/employee_survey_data.csv")
    print(data)
    print(data.head())
    print(data.info())
    print(data.describe())
    print(data.shape)
    print(data.columns)
    print(data.index)
    return data


data = import_data("XYZ Company/employee_survey_data.csv")
