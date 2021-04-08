

# Set index Employee ID
def set_index(column):
    set_index: data.set_index(column)
    print(set_index)
    return data

# Below works
data ["JobInvolvement"] = data["JobInvolvement"].replace({1:"Low", 2:"Medium", 3:"High", 4:"Very High"})
data ["PerformanceRating"] = data["PerformanceRating"].replace({1:"Low", 2:"Good", 3:"Excellent", 4:"Outstanding"})
print(data.head())

data.iloc[:, 1] = data.iloc[:, 1].apply(pd.to_datetime, errors = "coerce")
print(data.head())


# In Time
data = import_data("XYZ Company/in_time.csv")
clean_data(data)
data.iloc[:, 1] = data.iloc[:, 1].apply(pd.to_datetime, errors = "coerce")
print(data.head())
data = data.append



