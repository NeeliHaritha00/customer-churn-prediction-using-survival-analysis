# customer-churn-prediction
## Overview
This project focuses on predicting customer churn using survival analysis techniques. Churn prediction is crucial for businesses to retain their customers and maintain a healthy customer base. Survival analysis helps us understand the time until a customer churns and provides insights into retention strategies.

## Table of Contents

## Usage
Preprocess and explore your data by running Exploratory Data Analysis.ipynb.
Train and evaluate the survival analysis models using survival_analysis.ipynb.

## Data
**Telco Dataset**

This dataset contains information related to telecommunications customers, capturing various aspects such as customer demographics, services subscribed, usage patterns, and churn status. The dataset is useful for analyzing customer behavior, predicting churn, and gaining insights into the telecommunications industry.

**Columns**

**customerID** :
Unique identifier for each customer (object)

**gender** : 
Gender of the customer (object)

**SeniorCitizen** : 
Indicates if the customer is a senior citizen (int64)

**Partner** : 
Indicates if the customer has a partner (object)

**Dependents** : 
Indicates if the customer has dependents (object)

**tenure** : 
Number of months the customer has been with the company (int64)

**PhoneService** : 
Indicates if the customer has a phone service (object)

**MultipleLines**: 
Indicates if the customer has multiple lines (object)

**InternetService** : 
Type of internet service subscribed (object)

**OnlineSecurity** : 
Indicates if the customer has online security services (object)

**OnlineBackup** : 
Indicates if the customer has online backup services (object)

**DeviceProtection** : 
Indicates if the customer has device protection services (object)

**TechSupport** : 
Indicates if the customer has technical support services (object)

**StreamingTV** : 
Indicates if the customer has streaming TV services (object)

**StreamingMovies** : 
Indicates if the customer has streaming movie services (object)

**Contract** : 
Type of contract the customer has (object)

**PaperlessBilling** : 
Indicates if the customer uses paperless billing (object)

**PaymentMethod** : 
Payment method used by the customer (object)

**MonthlyCharges** : 
Monthly charges incurred by the customer (float64)

**TotalCharges** : 
Total charges incurred by the customer (object)

**Churn**
The Churn column indicates whether a customer has churned or not. "Churn" refers to customers who have discontinued their services with the company. It is a binary classification where 'Yes' means the customer has churned, and 'No' means the customer has not churned. Analyzing this column can provide insights into factors influencing customer retention and aid in developing strategies to reduce churn rates.

Find the dataset here https://www.kaggle.com/datasets/blastchar/telco-customer-churn

