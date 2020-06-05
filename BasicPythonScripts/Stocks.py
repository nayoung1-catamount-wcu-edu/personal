#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import pandas_datareader.data as web
import datetime as dt

# In[2]:


# Start for Stock series:
start = dt.datetime(2010, 1, 1)

# End of Stock series:
end = dt.datetime(2020, 12, 31)


# In[4]:


stocks_to_retrieve = ["IBM", "AAPL", "NFLX", "ORCL", "MSFT"]
df = web.DataReader(stocks_to_retrieve, "yahoo", start, end)
df.head()


# In[5]:


df_closing = df["Close"]
df_closing.head()


# In[12]:


df_closing.to_csv("C:/Users/natha/OneDrive/Desktop/GitHub/personal/Data/closing_stocks.csv")
