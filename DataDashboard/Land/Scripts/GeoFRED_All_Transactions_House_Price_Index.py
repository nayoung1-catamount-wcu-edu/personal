#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Imports
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine
import urllib
import numpy as np


# In[2]:


# Watermark
#print('Nathan Young\nJunior Data Analyst\nCenter for the Study of Free Enterprise')
#get_ipython().run_line_magic('load_ext', 'watermark')
#get_ipython().run_line_magic('watermark', '-a "Western Carolina University" -u -d -p pandas')


# In[3]:


# Create backups
#df_backup = pd.read_csv('./Updates/STG_FRED_All_Transactions_House_Price_Index.txt')
#df_backup.to_csv('./Backups/STG_FRED_All_Transactions_House_Price_Index_BACKUP.txt')


# In[4]:


# Getting and reading new data 
df = pd.read_excel("https://geofred.stlouisfed.org/api/download.php?theme=pubugn&colorCount=5&reverseColors=false&intervalMethod=fractile&displayStateOutline=true&lng=-90&lat=40&zoom=4&showLabels=true&showValues=true&regionType=county&seriesTypeId=942&attributes=Not+Seasonally+Adjusted%2C+Annual%2C+Index+2000%3D100&aggregationFrequency=Annual&aggregationType=Average&transformation=lin&date=2018-01-01&type=xls&startDate=1975-01-01&endDate=2018-01-01&mapWidth=999&mapHeight=1249&hideLegend=false", skiprows=1)
df.head(2)


# In[5]:


# Filter data to display only North Carolina
filter1 = df['Region Name'].str.contains(', NC')
df_nc = df[filter1]
df_nc.head(2)


# In[6]:


# Set Index to Series ID
df_nc.set_index(df_nc['Series ID'], inplace = True)
df_nc.head(2)


# In[7]:


# Drop Series ID column
df_nc.drop('Series ID', axis = 1, inplace = True)
df_nc.head(2)


# In[8]:


# Save file to tab delimited txt for upload to SSMS
#df_nc.to_csv('./Updates/STG_FRED_All_Transactions_House_Price_Index.txt', sep = '\t')


# In[9]:


#Reset Index for upload to database
df_nc = df_nc.reset_index()    


# In[ ]:


#Fill NaN values for upload to database
df_nc['Metro'] = df_nc['Metro'].replace(np.nan,'', regex=True)

column_list = df_nc.columns.values
for i in column_list:
    df_nc.loc[df_nc[i].isnull(),i]=0


# In[ ]:


#Connect to database and create cursor
con = pyodbc.connect('Driver={SQL Server};'
                      'Server=TITANIUM-BOOK;'
                      'Database=DataDashboard;'
                      'Trusted_Connection=yes;')

c = con.cursor()


# In[ ]:


#Drop old backup table
#c.execute('drop table STG_ZLLW_County_MedianValuePerSqft_AllHomes_BACKUP')


# In[ ]:


c.execute('''USE [DataDashboard]

SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[STG_ZLLW_County_MedianListingPrice_AllHomes](
	[RegionName] [varchar](40) NULL,
	[State] [varchar](2) NULL,
	[Metro] [varchar](40) NULL,
	[StateCodeFIPS] [varchar](2) NULL,
	[MunicipalCodeFIPS] [varchar](3) NULL,
	[SizeRank] [smallint] NULL,
	[2010-01] [float] NULL,
	[2010-02] [float] NULL,
	[2010-03] [float] NULL,
	[2010-04] [float] NULL,
	[2010-05] [float] NULL,
	[2010-06] [float] NULL,
	[2010-07] [float] NULL,
	[2010-08] [float] NULL,
	[2010-09] [float] NULL,
	[2010-10] [float] NULL,
	[2010-11] [float] NULL,
	[2010-12] [float] NULL,
	[2011-01] [float] NULL,
	[2011-02] [float] NULL,
	[2011-03] [float] NULL,
	[2011-04] [float] NULL,
	[2011-05] [float] NULL,
	[2011-06] [float] NULL,
	[2011-07] [float] NULL,
	[2011-08] [float] NULL,
	[2011-09] [float] NULL,
	[2011-10] [float] NULL,
	[2011-11] [float] NULL,
	[2011-12] [float] NULL,
	[2012-01] [float] NULL,
	[2012-02] [float] NULL,
	[2012-03] [float] NULL,
	[2012-04] [float] NULL,
	[2012-05] [float] NULL,
	[2012-06] [float] NULL,
	[2012-07] [float] NULL,
	[2012-08] [float] NULL,
	[2012-09] [float] NULL,
	[2012-10] [float] NULL,
	[2012-11] [float] NULL,
	[2012-12] [float] NULL,
	[2013-01] [float] NULL,
	[2013-02] [float] NULL,
	[2013-03] [float] NULL,
	[2013-04] [float] NULL,
	[2013-05] [float] NULL,
	[2013-06] [float] NULL,
	[2013-07] [float] NULL,
	[2013-08] [float] NULL,
	[2013-09] [float] NULL,
	[2013-10] [float] NULL,
	[2013-11] [float] NULL,
	[2013-12] [float] NULL,
	[2014-01] [float] NULL,
	[2014-02] [float] NULL,
	[2014-03] [float] NULL,
	[2014-04] [float] NULL,
	[2014-05] [float] NULL,
	[2014-06] [float] NULL,
	[2014-07] [float] NULL,
	[2014-08] [float] NULL,
	[2014-09] [float] NULL,
	[2014-10] [float] NULL,
	[2014-11] [float] NULL,
	[2014-12] [float] NULL,
	[2015-01] [float] NULL,
	[2015-02] [float] NULL,
	[2015-03] [float] NULL,
	[2015-04] [float] NULL,
	[2015-05] [float] NULL,
	[2015-06] [float] NULL,
	[2015-07] [float] NULL,
	[2015-08] [float] NULL,
	[2015-09] [float] NULL,
	[2015-10] [float] NULL,
	[2015-11] [float] NULL,
	[2015-12] [float] NULL,
	[2016-01] [float] NULL,
	[2016-02] [float] NULL,
	[2016-03] [float] NULL,
	[2016-04] [float] NULL,
	[2016-05] [float] NULL,
	[2016-06] [float] NULL,
	[2016-07] [float] NULL,
	[2016-08] [float] NULL,
	[2016-09] [float] NULL,
	[2016-10] [float] NULL,
	[2016-11] [float] NULL,
	[2016-12] [float] NULL,
	[2017-01] [float] NULL,
	[2017-02] [float] NULL,
	[2017-03] [float] NULL,
	[2017-04] [float] NULL,
	[2017-05] [float] NULL,
	[2017-06] [float] NULL,
	[2017-07] [float] NULL,
	[2017-08] [float] NULL,
	[2017-09] [float] NULL,
	[2017-10] [float] NULL,
	[2017-11] [float] NULL,
	[2017-12] [float] NULL,
	[2018-01] [float] NULL,
	[2018-02] [float] NULL,
	[2018-03] [float] NULL,
	[2018-04] [float] NULL,
	[2018-05] [float] NULL,
	[2018-06] [float] NULL,
	[2018-07] [float] NULL,
	[2018-08] [float] NULL,
	[2018-09] [float] NULL,
	[2018-10] [float] NULL,
	[2018-11] [float] NULL,
	[2018-12] [float] NULL,
	[2019-01] [float] NULL,
	[2019-02] [float] NULL,
	[2019-03] [float] NULL,
	[2019-04] [float] NULL,
	[2019-05] [float] NULL,
	[2019-06] [float] NULL,
	[2019-07] [float] NULL,
	[2019-08] [float] NULL,
	[2019-09] [float] NULL,
	[2019-10] [float] NULL,
	[2019-11] [float] NULL,
	[2019-12] [float] NULL,
    [2020-01] [float] NULL,
    [2020-02] [float] NULL,
    [2020-03] [float] NULL,
    [2020-04] [float] NULL,
    [2020-05] [float] NULL,
    [2020-06] [float] NULL,
    [2020-07] [float] NULL,
    [2020-08] [float] NULL,
    [2020-09] [float] NULL,
    [2020-10] [float] NULL,
    [2020-11] [float] NULL,
    [2020-12] [float] NULL
) ON [PRIMARY]''')


# In[ ]:


con.commit()


# In[ ]:


from sqlalchemy import create_engine
params = urllib.parse.quote_plus(r'Driver={SQL Server};' 
                                 r'Server=TITANIUM-BOOK;'
                                 r'Database=DataDashboard;'
                                 r'Trusted_Connection=yes;')

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

#df: pandas.dataframe; mTableName:table name in MS SQL
#warning: discard old table if exists
df_nc.to_sql('STG_ZLLW_County_MedianListingPrice_AllHomes', con=engine, if_exists='replace', index=False)

