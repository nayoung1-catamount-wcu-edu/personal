#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

import pandas_datareader.data as web
import datetime as dt


# In[4]:


import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf
cf.set_config_file(offline=True)


# In[5]:


# Start for Stock series:
start = dt.datetime(1980, 1, 1)

# End of Stock series:
end = dt.datetime(2020, 12, 31)


# In[6]:


stocks_to_retrieve = [
    'MMM',
    'AXP',
    'AAPL',
    'BA',
    'CAT',
    'CVX',
    'CSCO',
    'KO',
    'DIS',
    'DOW',
    'XOM',
    'GS',
    'HD',
    'IBM',
    'INTC',
    'JNJ',
    'JPM',
    'MCD',
    'MRK',
    'MSFT',
    'NKE',
    'PFE',
    'PG',
    'TRV',
    'UTX',
    'UNH',
    'VZ',
    'V',
    'WMT',
    'WBA']
#stocks_to_retrieve = ['DJIA']
df = web.DataReader(stocks_to_retrieve, 'yahoo', start, end)
df.head()


# In[7]:


df_closing = df['Close']
df_closing.head()


# In[8]:


df_closing.iplot(kind='line',
                 title='DOW Close: 01/1900-06/2020')


# In[ ]:

df_closing.to_csv('C:/Users/natha/OneDrive/Desktop/personal/Data/closing_stocks.csv')
