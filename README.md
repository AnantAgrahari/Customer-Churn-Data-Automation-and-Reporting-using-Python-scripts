# Customer Churn Analysis Automation (Python)

## Overview
This project automates customer churn analysis using Python. It processes raw customer data, performs data cleaning and validation, computes key churn and revenue metrics, and logs execution details. The script is designed to simulate a real-world analytics automation pipeline that can be scheduled to run periodically.

---

## Business Objective
Customer churn directly impacts revenue and long-term growth. This automation enables consistent monitoring of churn behavior and customer value by generating reliable KPIs without manual intervention.

---

## Tech Stack
- Python  
- Pandas  
- Logging module  
- Command Line (CMD)  

---

## Dataset
**Telco Customer Churn Dataset (CSV)**

Key columns used:
- `customerID`
- `Churn`
- `tenure`
- `MonthlyCharges`
- `TotalCharges`

---

## Automation Workflow

### 1. Data Ingestion
- Reads customer churn data from CSV
- Logs successful data loading

### 2. Data Cleaning
- Converts `TotalCharges` from object to numeric
- Handles blank and missing values
- Ensures consistent data types

### 3. Data Validation
- Checks presence of required columns
- Raises errors if schema validation fails

### 4. KPI Computation
- Total customers
- Churned vs retained customers
- Churn rate (%)
- Average tenure (churned vs non-churned)
- Average monthly charges (churned vs non-churned)

### 5. Logging & Error Handling
- Logs execution steps and errors
- Creates a persistent log file for monitoring

---

## Key Outputs
- Customer churn rate
- Revenue and tenure comparison
- Statistical summaries of monthly charges
- Execution logs for debugging and audits

---

