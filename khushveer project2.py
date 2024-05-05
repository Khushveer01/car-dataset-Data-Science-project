#!/usr/bin/env python
# coding: utf-8

# # WORKING ON REAL PROJECT WITH PYTHON

# # Cars Dataset

# Here the data of different cars is given with the specifications
# This data is available as a CSV file.We are going to analyze this data set using the Pandas DataFrame

# In[5]:


import pandas as pd


# In[6]:


car=pd.read_csv(r"C:\Users\KHUSHVEER SINGH\Downloads\2. Cars Data1.csv")


# In[10]:


car.head()


# In[9]:


car.shape


# 1)Instruction(For Data Cleaning)
# Find the Null Value in the dataset.If there is any null value in any column.then fill it with the mean of that column

# In[9]:


car.isnull().sum()


# In[12]:


car['Cylinders'].fillna(car['Cylinders'].mean(),inplace=True)


# In[13]:


car


# 2)Question(Based on Value Counts)
# Check what are the different types of make are there in our dataset and what is the count (ocurrence) of each make in the data

# In[11]:


car.head(2)


# In[15]:


car['Make'].value_counts()


# 3)Instruction(Filtering)
# Show all the records where Origin is Asia and Europe

# In[16]:


car.head(2)


# In[18]:


car[car['Origin'].isin(['Asia','Europe'])]


# 4)Instruction(Removing unwanted records)
# Remove all the records (rows) where Weight is above 4000

# In[19]:


car.head(2)


# In[25]:


car[~(car['Weight']>4000)]


# In[26]:


432-103


# 5)Insruction(Appyling function on a column)
# Increase all the values of'MPG_City' column by 3

# In[27]:


car.head(2)


# In[30]:


car['MPG_City']=car['MPG_City'].apply(lambda x:x+3)


# In[31]:


car


# In[ ]:




