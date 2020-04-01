#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv('D:\programming Python\Stepic Machine leaning 02.2020\Iris.csv')


# In[4]:


df


# In[35]:


df=df.drop('Unnamed: 0', axis=1)


# In[36]:


df


# In[37]:


for column in df:
    sns.kdeplot(df[column])


# In[40]:


sns.violinplot(df['petal width'])


# In[39]:


sns.violinplot(df['petal length'], orient='v')


# In[41]:


sns.pairplot(df)


# In[42]:


sns.pairplot(df, hue='species')


# In[ ]:




