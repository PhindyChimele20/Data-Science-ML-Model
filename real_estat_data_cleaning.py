#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Import all packages to be used
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
matplotlib.rcParams["figure.figsize"] = (20,10)


# In[3]:


#Create a dataframe from data
df = pd.read_csv("C:/Users/phind/OneDrive/Documents/data_science_projects/archive/Bengaluru_House_Data.csv")
#View the df
df.head() 


# In[4]:


#check the number of rows and columns in the data
df.shape


# In[5]:


#Examine the area type feature, group the dataframe by area type then aggregate the count
df.groupby('area_type')['area_type'].agg('count')


# In[7]:


#To keep model simple, drop columns/features that are not important
df2 = df.drop(['area_type', 'society', 'balcony', 'availability'],axis='columns')
df2.head()


# In[8]:


#Data cleaning
#Remove missing (Na) values
df2.isnull().sum() #count the no of rows with missing values



# In[9]:


#Drop missing values (if the missing values are a lot you can replace missing values with the median)
df3 = df2.dropna()
df3.isnull().sum()


# In[11]:


#Explore the siza feature
df3['size'].unique()


# In[12]:


df3['bhk'] = df3['size'].apply(lambda x: int(x.split(' ')[0]))


# In[13]:


df3.head()


# In[14]:


df3['bhk'].unique()


# In[15]:


#view bhk/bedrooms greater than 20
df3[df3.bhk>20]


# In[16]:


#explore the total sqft feature
df3.total_sqft.unique()


# In[19]:


#Check the type of variation in the total sqft feature
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True


# In[20]:


df3[df3['total_sqft'].apply(is_float)].head()


# In[22]:


#return values without a valid float
df3[~df3['total_sqft'].apply(is_float)].head(10)


# In[30]:


#Convert range values into a single value by averaging
def convert_sqft_to_num(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
            return float(x)
    except:
            return None


# In[26]:


convert_sqft_to_num('2166')


# In[31]:


convert_sqft_to_num('2100 - 2850')


# In[32]:


convert_sqft_to_num('4125Perch')


# In[33]:


df4 = df3.copy()
df4['total_sqft'] = df4['total_sqft'].apply(convert_sqft_to_num)
df4.head(3)


# In[34]:


df4.loc[30]


# In[ ]:




