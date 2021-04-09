# Date Drop in Timestamp
def drop(columns):
    drop = data.drop([columns], axis=1, inplace=True)
    print(drop.head())
    return data

add again
#TOMORROW - Try drop dates in timestamps

# Out Time
data = import_data("XYZ Company/out_time.csv")
clean_data(data)
rename("Unnamed: 0")
data.iloc[:, 1] = data.iloc[:, 1].apply(pd.to_datetime, errors = "coerce")
print(data.head())

# In Time
data = import_data("XYZ Company/in_time.csv")
clean_data(data)
rename("Unnamed: 0")
data.iloc[:, 1] = data.iloc[:, 1].apply(pd.to_datetime, errors = "coerce")
print(data.head())

# Out Time
data = import_data("XYZ Company/out_time.csv")
clean_data(data)
rename("Unnamed: 0")
data.iloc[:, 1] = data.iloc[:, 1].apply(pd.to_datetime, errors = "coerce")
print(data.head())

# In Time
data = import_data("XYZ Company/in_time.csv")
clean_data(data)
rename("Unnamed: 0")
data.iloc[:, 1] = data.iloc[:, 1].apply(pd.to_datetime, errors = "coerce")
print(data.head())

works:
data.drop(["EmployeeCount", "StandardHours", "Over18", "MaritalStatus"], axis=1, inplace=True)
print(data.shape)