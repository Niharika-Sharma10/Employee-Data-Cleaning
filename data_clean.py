import pandas as pd
import numpy as np
# loading the dataset
df=pd.read_csv(r"d:\Profiles\Harsh\Downloads\indian_employee_data_clean.csv")
print(df.head())
print(df.tail())
# checking the missing values
print("Missing values in dataset")
print(df.isnull().sum())
# handle missing values with avg
print("Handle missing values")
df["Salary (INR)"] = df["Salary (INR)"].fillna(df["Salary (INR)"].mean())
df["Performance Rating"]=df["Performance Rating"].fillna(df["Performance Rating"].median())
# infinite value check
df.replace([np.inf,-np.inf],np.nan,inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)
# duplicate value handle
df.drop_duplicates(inplace=True)
# replace  negative salaries
df["Salary (INR)"]= np.where(df["Salary (INR)"]<0, df["Salary (INR)"].mean(),df["Salary (INR)"])

salary_mean = df["Salary (INR)"].mean()
salary_std = df["Salary (INR)"].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[
    (df["Salary (INR)"] >= lower_bound) &
    (df["Salary (INR)"] <= upper_bound)
]
df.to_csv("cleaned_indian_employee_data.csv", index=False)
print("Data cleaning completed!")
