#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


event_data=pd.read_csv('D:\programming Python\Stepic Machine leaning 02.2020\event_data_train.csv')


# In[3]:


event_data['date']=pd.to_datetime(event_data.timestamp, unit='s')


# In[4]:


event_data['month']=event_data['date'].dt.month
event_data['year']=event_data['date'].dt.year


# In[5]:


event_data


# In[6]:


event_data[event_data['user_id']==1046]


# In[7]:


event_data.groupby('user_id').agg({'month':'count'}).sort_values(by='month')


# In[8]:


event_data_2016=event_data[event_data.year==2016]


# In[9]:


event_data_2016.groupby('user_id').agg({'month':'count'})


# In[10]:


event_data


# In[ ]:


event_data2016_month_ye


# # 

# In[124]:


submissions=pd.read_csv('D:\programming Python\Stepic Machine leaning 02.2020\submissions_data_train.csv')


# In[125]:


submissions


# In[133]:


submissions[submissions.submission_status == 'correct'].groupby('user_id').agg({'submission_status': 'count'}).sort_values(by=['submission_status'], ascending=False).head(20)


# In[ ]:




