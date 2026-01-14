# Customer-Churn-Data-Automation-Reporting-using-Python-scripts
Customer Churn Analysis Automation (Python)
Overview

This project automates customer churn analysis using Python. It processes raw customer data, performs data cleaning and validation, computes key churn and revenue metrics, and logs execution details. The script is designed to simulate a real-world analytics automation pipeline that can be scheduled to run periodically.

Business Objective

Customer churn has a direct impact on revenue and retention strategies. This automation enables consistent monitoring of churn behavior and customer value by generating reliable KPIs without manual intervention.

Tech Stack

Python

Pandas

Logging module

Command Line (CMD) execution

Dataset

Telco Customer Churn Dataset

Format: CSV

Key fields:

customerID

Churn

tenure

MonthlyCharges

TotalCharges

Automation Flow
1. Data Ingestion

Loads customer churn data from CSV

Logs successful file loading

2. Data Cleaning

Converts TotalCharges from object to numeric

Handles blank and missing values

Ensures data consistency

3. Data Validation

Verifies presence of mandatory columns

Stops execution if schema validation fails

4. KPI Computation

Total customers

Churned vs retained customers

Churn rate

Average tenure (churned vs non-churned)

Average monthly charges (churned vs non-churned)

5. Logging & Error Handling

Logs execution status and errors

Creates a persistent log file for monitoring

Key Outputs

Churn rate percentage

Revenue and tenure comparison between churned and retained customers

Statistical summaries for monthly charges

Execution logs for audit and debugging
