import pandas as pd
file_path="WA_Fn-UseC_-Telco-Customer-Churn.csv"

df=pd.read_csv(file_path)
print(df.head())

print(df.dtypes)

blank_count=(df.TotalCharges==' ').sum()
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')

df['TotalCharges'].fillna(0,inplace=True)

print(df.dtypes)
print(df.isnull().sum())

