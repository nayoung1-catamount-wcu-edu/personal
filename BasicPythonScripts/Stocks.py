#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd

import pandas_datareader.data as web
import datetime as dt


# In[3]:


import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
cf.set_config_file(offline=True)


# In[2]:


# Start for Stock series:
start = dt.datetime(2010, 1, 1)

# End of Stock series:
end = dt.datetime(2019, 12, 31)


# In[4]:


stocks_to_retrieve = ['IBM', 'AAPL', 'NFLX', 'ORCL', 'MSFT']
df = web.DataReader(stocks_to_retrieve, 'yahoo', start, end)
df.head()


# In[5]:


df_closing = df['Close']
df_closing.head()


# In[6]:


df_closing.plot()


# In[7]:


df_closing.iplot(kind='line',
                title='Apple, IBM, Netflix, Microsoft, and Oracle Close: 01/2010-11/2019')


# In[12]:


df_closing.to_csv('C:/Users/natha/OneDrive/Desktop/personal/Data/closing_stocks.csv')

