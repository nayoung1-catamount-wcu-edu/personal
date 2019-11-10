#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[54]:


import pandas as pd


# # Bible Verse Data

# ### Load and view file in dataframe

# In[55]:


df = pd.read_excel('/Users/owner/Onedrive/Desktop/personal/Data/bible_kjv.xlsx')

df.head(2)


# ### View and edit columns

# In[56]:


df.columns


# In[57]:


rename_columns = {'b':'book',
                 'c':'chapter',
                 'v':'verse',
                 't':'text'}

df.rename(columns = rename_columns, inplace=True)
df.head(2)


# ### View and edit datatypes

# In[58]:


df.dtypes


# In[59]:


df['book']=pd.to_numeric(df['book']).astype(object)
df.dtypes


# # Books of the Bible Data

# ### Load and view file in dataframe

# In[60]:


df_books = pd.read_excel('/Users/owner/Onedrive/Desktop/personal/Data/bible_books.xlsx')

df_books.head(2)


# ### View and edit columns

# In[61]:


df_books.columns


# ### View and edit datatypes

# In[62]:


df_books.dtypes


# # Merge

# ### Left-joining Bible Verse Data with Books Data to create complete Bible database

# In[63]:


df_bible = pd.merge(df_books, df, on = 'book', how = 'left')
df_bible.head()


# ### Editing columns in new dataframe

# In[64]:


new_column_order = ['id','book','book_name','chapter','verse','text']

df_bible = df_bible[new_column_order]

print('Number of rows: ',df_bible.shape[0])
print('Number of columns: ',df_bible.shape[1])
df_bible.head()


# In[65]:


df_bible.to_csv('/Users/owner/Onedrive/Desktop/personal/Data/finished_bible.csv')

