#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[58]:


sns.set(style="white")
sns.set_palette('gist_earth')


# In[3]:


telco=pd.read_csv('E:\\Telco-Customer-Churn.csv')


# In[4]:


telco.info()


# In[5]:


telco


# In[6]:


telco.shape


# In[7]:


telco.isnull().sum()


# In[8]:


telco[telco.duplicated()]


# In[9]:


object_type=[]
for column_name in telco.columns:
    if telco[column_name].dtype=='object':
        object_type.append(column_name)


# In[10]:


for i in object_type:
    print('col name: ',i)
    print('Missing values : ',telco[i].isnull().sum())
    print('No of Unique values : ' ,telco[i].nunique())
    print('Unique values : ',telco[i].unique())
    print('----------------------------')


# # Analysis

# **customerID**

# Removing CustomerID as it doesnot give any information about customer churning

# In[11]:


telco.drop('customerID',axis=1,inplace=True)


# In[12]:


def stacked_plot(col_name,target_col,df):
    plt.rcParams['figure.facecolor'] = 'white'  # Set the background color of the figure

    plt.figure(figsize=(6,4))
    crosstab = pd.crosstab(df[col_name], df[target_col],normalize='index')
    crosstab.plot(kind='bar', stacked=True)
    plt.title(f'{col_name} vs {target_col}')
    plt.xlabel(col_name)
    plt.ylabel(target_col)
    plt.xticks(rotation=45)
    plt.gca().set_facecolor('#000000')  
    plt.show()


# In[13]:


crosstab = pd.crosstab(telco['SeniorCitizen'], telco['Churn'],normalize='index')


# In[14]:


crosstab


# **gender,SeniorCitizen,Partner,Dependents**

# In[17]:


stacked_plot('gender','Churn',telco)
stacked_plot('SeniorCitizen','Churn',telco)
stacked_plot('Partner','Churn',telco)
stacked_plot('Dependents','Churn',telco)


# In[18]:


telco.groupby(['SeniorCitizen','Partner','Dependents','Churn']).size()/telco.groupby('SeniorCitizen')['Churn'].count()#3641 no= yes 32.9 yes =yes 

From the plots above,we can see that
1) gender (Male,Female) have same effect on churn and hence doesnot help much in churn prediction
2) young people(SeniorCitizen=0)
     ---> with no family are more churning (no partner no dependent)
   Old people(seniorCitizen=1)
     ---> without family are more churning(no-no) 
     ---> with family less churning(atleast one yes)
# **tenure**

# In[19]:


sns.set(style="white")
sns.set_palette('jet_r')
plt.figure(figsize=(16,8))
sns.countplot(x="tenure", hue="Churn", data=telco)
plt.gca().set_facecolor('#000000')
plt.show()

As we can see,churn rate is decreasing with tenure increasing,which means customer becomes loyalReducing the values into 6 groups for better understanding
# In[20]:


def tenure(t):
    if t<=12:
        return 1
    elif t>12 and t<=24:
        return 2
    elif t>24 and t<=36:
        return 3
    elif t>36 and t<=48:
        return 4
    elif t>48 and t<=60:
        return 5
    else:
        return 6

telco["tenure_group"]=telco["tenure"].apply(lambda x: tenure(x))


# In[21]:


telco["tenure_group"].value_counts()


# In[26]:


sns.set(style="white")
sns.set_palette('turbo')
plt.figure(figsize=(6,5))
sns.countplot(x="tenure_group", hue="Churn", data=telco)
plt.gca().set_facecolor('#000000')
plt.show()


# **Phoneservice and MultipleLines**

# In[27]:


stacked_plot('PhoneService','Churn',telco,)
stacked_plot('MultipleLines','Churn',telco)


# In[28]:


telco.groupby(['PhoneService','Dependents'])['Churn'].count()/telco.groupby('PhoneService')['Dependents'].count()
#stats for each category are same  for Seniorcitizen and dependents 

from the stats,we can see that churn is almost same for all categories.Hence PhoneService and MultipleLines doesnot help much in churn prediction
# **InternetService**

# In[30]:


stacked_plot('InternetService','Churn',telco)

churn rate is high for fibre optic compared to DSL and no internet service, maybe due high cost 
# In[31]:


#telco.groupby(['InternetService','SeniorCitizen','Churn']).size()
data = (telco.groupby(['InternetService','Dependents'])['Churn'].count() / telco.groupby('InternetService')['Churn'].count()).reset_index()

# Create a bar chart
plt.figure(figsize=(5,4))
plt.bar(data.index, data['Churn'])
plt.xticks(data.index, data['InternetService'] + ' - ' + data['Dependents'].astype(str))
plt.xlabel('InternetService - Dependents')
plt.ylabel('Churn Percentage')
plt.title('Churn Percentage by InternetService and Dependents')
plt.xticks(rotation=45)
plt.show()


# In[32]:


telco.groupby(['InternetService','Dependents','Churn']).size()/telco.groupby(['InternetService','Dependents'])['Churn'].count()

nwe can see that phone service, senior citizen cant explain the churning in fiber optic
using dependents we can analyze that customers with no family are more churning compared to with family but overall churning is high regardless for fiber optic
# In[33]:


sns.set(style="white")
sns.histplot(data=telco[telco.InternetService == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.InternetService == "DSL"],x='tenure',label="DSL",kde=True,color='orange')
sns.histplot(data=telco[telco.InternetService == "Fiber optic"],x='tenure',label="Fiber optic",kde=True,color='grey')
plt.title("Tenure Distribution by Internet Service type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()

the tenure distribution of customers with different internet service is similar.
# **OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV,StreamingMovies**

# In[36]:


stacked_plot('OnlineSecurity','Churn',telco)
stacked_plot('OnlineBackup','Churn',telco)
stacked_plot('DeviceProtection','Churn',telco)
stacked_plot('TechSupport','Churn',telco)
stacked_plot('StreamingTV','Churn',telco)
stacked_plot('StreamingMovies','Churn',telco) 

customers with no OnlineSecurity is more churning
the churning in OnlineSecurity for  yes is due to fiber optic InternetService
for no both dsl and fiber optic is causing churning
# In[37]:


telco.groupby(['StreamingMovies','InternetService','Churn']).size()/telco.groupby(['StreamingMovies','InternetService'])['Churn'].count()


# In[38]:


sns.set(style="white")
sns.histplot(data=telco[telco.OnlineSecurity == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.OnlineSecurity == "No internet service"],x='tenure',label="No internet service",kde=True,color='orange')
sns.histplot(data=telco[telco.OnlineSecurity == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution by OnlineSecurity type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()


# In[39]:


sns.set(style="white")
sns.histplot(data=telco[telco.OnlineBackup == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.OnlineBackup == "No internet service"],x='tenure',label="No internet service",kde=True,color='orange')
sns.histplot(data=telco[telco.OnlineBackup == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution by OnlineBackup type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()


# In[40]:


sns.set(style="white")
sns.histplot(data=telco[telco.DeviceProtection == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.DeviceProtection == "No internet service"],x='tenure',label="No internet service",kde=True,color='orange')
sns.histplot(data=telco[telco.DeviceProtection == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution by DeviceProtection type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()


# In[41]:


sns.set(style="white")
sns.histplot(data=telco[telco.TechSupport == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.TechSupport == "No internet service"],x='tenure',label="No internet service",kde=True,color='orange')
sns.histplot(data=telco[telco.TechSupport == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution by TechSupport type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()


# In[42]:


sns.set(style="white")
sns.histplot(data=telco[telco.StreamingTV == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.StreamingTV == "No internet service"],x='tenure',label="No internet service",kde=True,color='orange')
sns.histplot(data=telco[telco.StreamingTV == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution by StreamingTV type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()


# In[43]:


sns.set(style="white")
sns.histplot(data=telco[telco.StreamingMovies == "No"],x='tenure',label="No",kde=True,color='green')
sns.histplot(data=telco[telco.StreamingMovies == "No internet service"],x='tenure',label="No internet service",kde=True,color='orange')
sns.histplot(data=telco[telco.StreamingMovies == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution by StreamingMovies type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()

when the customers are new they do not opt for various services and their churning rate is very high.Customers that opt services tend to stay longer.
This suggests that offering services may have a positive impact on customer retention.
# In[44]:


#with tenure and internet services

sns.set_palette('cubehelix')
data_no = telco[telco['StreamingTV'] == "No"]
data_yes = telco[telco['StreamingTV'] == "Yes"]
data_no_internet = telco[telco['StreamingTV'] == "No internet service"]
# Create a histogram for the 'tenure' column in the filtered data
sns.histplot(data=data_no, x='tenure', kde=True, label='No',color='orange')
sns.histplot(data=data_yes, x='tenure', kde=True, label='yes',color='green')
sns.histplot(data=data_no_internet, x='tenure', kde=True, label='No internet service',color='darkred')
plt.title("Tenure Distribution for OnlineSecurity = No")
plt.gca().set_facecolor('#000000')
plt.legend()
plt.show()


# **Contract**

# In[46]:


stacked_plot('Contract','Churn',telco)

customers that opt to month to month contract churn the most
# In[47]:


telco.groupby(['Contract','InternetService','Churn'])['Churn'].size()/telco.groupby(['Contract','InternetService'])['Churn'].count()

customers who with month to month contract and opted Fiber optic are more churning  
# In[48]:


sns.set(style="white")
sns.histplot(data=telco[telco.Contract == "Month-to-month"],x='tenure',label="Month-to-month",kde=True,color='green')
sns.histplot(data=telco[telco.Contract == "One year"],x='tenure',label="One year",kde=True,color='orange')
sns.histplot(data=telco[telco.Contract == "Two year"],x='tenure',label="Two year",kde=True,color='grey')
plt.title("Tenure Distribution by Contract type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()

new customers tend to opt Month-to-month contract more 
# **PaperlessBilling**

# In[51]:


stacked_plot('PaperlessBilling','Churn',telco)


# In[52]:


telco.groupby(['PaperlessBilling','InternetService','Churn'])['Churn'].count()/telco.groupby(['PaperlessBilling','InternetService'])['Churn'].count()


# In[53]:


stacked_plot('PaperlessBilling','Contract',telco)


# In[54]:


telco.groupby(['PaperlessBilling','InternetService','Contract','Churn'])['Churn'].count()/telco.groupby(['PaperlessBilling','InternetService','Contract'])['Churn'].count()

customers who chose Paperless billing , regardless of what internet service they choose are churning
customers who opted Month to month contract are more churning 
# In[55]:


sns.set(style="white")
sns.histplot(data=telco[telco.PaperlessBilling == "No"],x='tenure',label="No",kde=True,color='orange')
sns.histplot(data=telco[telco.PaperlessBilling == "Yes"],x='tenure',label="yes",kde=True,color='grey')
plt.title("Tenure Distribution PaperlessBilling type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()

the underlying patterns and trends in how long customers stay with the service are similar for both groups.
# **PaymentMethod** 

# In[56]:


telco['PaymentMethod'].value_counts()


# In[59]:


stacked_plot('PaymentMethod','Churn',telco)


# In[60]:


telco.groupby(['PaymentMethod','InternetService','Churn'])['Churn'].count()/telco.groupby(['PaymentMethod','InternetService'])['Churn'].count()


# In[61]:


stacked_plot('PaymentMethod','Contract',telco)


# In[62]:


telco.groupby(['PaymentMethod','Contract','Churn'])['Churn'].count()/telco.groupby(['PaymentMethod','Contract'])['Churn'].count()

churn is high for Electronic Check PaymentMethod regardless of internet service
customers who chose month to month contract and chose Electronic check as payment method are more churning.
# In[63]:


telco.groupby(['PaymentMethod','PaperlessBilling','Churn'])['Churn'].count()/telco.groupby(['PaymentMethod','PaperlessBilling'])['Churn'].count()


# In[64]:


sns.set(style="white")
sns.histplot(data=telco[telco.PaymentMethod == "Bank transfer (automatic)"],x='tenure',label="Bank transfer (automatic)",kde=True,color='red')
sns.histplot(data=telco[telco.PaymentMethod == "Credit card (automatic)"],x='tenure',label="Credit card (automatic)",kde=True,color='orange')
sns.histplot(data=telco[telco.PaymentMethod == "Electronic check"],x='tenure',label="Electronic check",kde=True,color='grey')
sns.histplot(data=telco[telco.PaymentMethod == "Mailed check"],x='tenure',label="Mailed check",kde=True,color='green')
plt.title("Tenure Distribution PaymentMethod type")
plt.gca().set_facecolor('#ffffff')
plt.legend()
plt.show()

new customers opt to Electronic check morepaperlessbilling kde plots similarity
paperlessbilling and payment method
# **MonthlyCharges**

# In[65]:


telco['MonthlyCharges'].describe()


# In[66]:


churned=telco[telco['Churn']=='Yes']
not_churned=telco[telco['Churn']=='No']


# In[67]:


sns.kdeplot(data=churned,x='MonthlyCharges', label = "Churned")
sns.kdeplot(data=not_churned,x='MonthlyCharges', label = "Churned")
plt.legend()
plt.gca().set_facecolor('#000000')
plt.show()

customers paying high monthly charges churn more
# **TotalCharges**

# In[68]:


telco['TotalCharges'].describe()


# In[69]:


telco['TotalCharges'].isnull().sum()


# In[70]:


telco['TotalCharges'] = telco["TotalCharges"].replace(" ",np.nan)
telco['TotalCharges'].isna().sum() 


# In[71]:


telco[telco["TotalCharges"].isnull()]

customers with missing total charges has tenure=0,hence filling the missing values with 0
# In[72]:


telco['TotalCharges'].fillna(0,inplace=True)


# In[73]:


telco['TotalCharges'].astype(float)


# In[74]:


sns.kdeplot(data=churned,x='tenure',label='churned')
sns.kdeplot(data=not_churned,x='tenure',label='not_churned')
plt.legend()
plt.gca().set_facecolor('#000000')
plt.show()

The density of total charges for churning customers are high around 0. As many customers cancel the service in 1 or 2 months time
# # Function to Pre-process the data 
# 

# In[75]:


def data_pre_processing(filepath):
    df = pd.read_csv(filepath)
    df.drop(["customerID"], inplace=True, axis=1)

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce').fillna(0)

    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling', 'Churn', 'PhoneService']
    df[binary_cols] = df[binary_cols].replace({'No': 0, 'Yes': 1})

    df['gender'] = df['gender'].replace({'Male': 0, 'Female': 1})
    

    binary_mapping = {'No phone service': 0,'No internet service': 0 ,'No': 0, 'Yes': 1}
    df['MultipleLines'] = df['MultipleLines'].replace(binary_mapping)

    cols2 = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

    for col in cols2:
        df[col] = df[col].replace(binary_mapping)
    df = pd.get_dummies(df, columns=['InternetService', 'Contract', 'PaymentMethod'], drop_first=True)
#If a column has only two unique categories and there is a meaningful ordinal relationship,binary encoding might be more suitable.
#If a column has more than two categories or there is no meaningful ordinal relationship, one-hot encoding is often preferred.

    return df


# In[76]:


data_pre_processing('E:\\Telco-Customer-Churn.csv')

