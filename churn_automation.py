# Loads the CSV files

import pandas as pd
file_path="WA_Fn-UseC_-Telco-Customer-Churn.csv"

df=pd.read_csv(file_path)
print(df.head())

# Data Cleaning process

print(df.dtypes)

blank_count=(df.TotalCharges==' ').sum()
df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')

df['TotalCharges'].fillna(0,inplace=True)

print(df.dtypes)
print(df.isnull().sum())

# Validates the table data 

print("Rows:",df.shape[0])
print("Columns:", df.shape[1])

required_columns=["TotalCharges","MonthlyCharges","Churn","customerID","tenure"]

# Checks for missing columns

missing_cols=[col for col in required_columns if col not in df.columns]

# Raises an error if any of the missing cols are found

if missing_cols:
  raise ValueError(f'Missing required columns:{missing_cols}')

# Dataframe split into Churned and Unchurned segments

Churned=df[df["Churn"]=="Yes"]
Unchurned=df[df["Churn"]=="No"]

# Customer counts KPIs

total_customers= df.shape[0]
churned_cust=Churned.shape[0]
unchurned_cust=Unchurned.shape[0]
churn_rate=churned_cust/total_customers*100

# Revenue related KPIs

avg_tenure_churned= Churned["tenure"].mean()
avg_tenure_unchurned=Unchurned["tenure"].mean()

avg_monthlycharges_churned=Churned["MonthlyCharges"].mean()
avg_monthlycharges_unchurned=Unchurned["MonthlyCharges"].mean()

# Key insights

print("\n---Churn Summary---")
print(f"Total Customers : {total_customers}")
print(f"Churned customers: {churned_cust}")
print(f"Unchurned customers: {unchurned_cust}")
print(f"Churn rate:{churn_rate}")
print("\n----Key KPIs---")
print(f"Avg churn tenure:{avg_tenure_churned}")
print(f"Avg unchurn tenure:{avg_tenure_unchurned}")
print(f"Avg monthlycharges churn:{avg_monthlycharges_churned}")
print(f"Avg monhtlycharges unchurned:{avg_monthlycharges_unchurned}")


