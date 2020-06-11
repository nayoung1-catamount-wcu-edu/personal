#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import pandas as pd
import random


# # Bible Verse Data

# ### Load and view file in dataframe

# In[2]:


df = pd.read_excel(
    '/Users/natha/Onedrive/Desktop/GitHub/personal/Data/bible_kjv.xlsx')

df.head(2)


# ### View and edit columns

# In[3]:


df.columns


# In[4]:


rename_columns = {'b': 'book',
                  'c': 'chapter',
                  'v': 'verse',
                  't': 'text'}

df.rename(columns=rename_columns, inplace=True)
df.head(2)


# ### View and edit datatypes

# In[5]:


df.dtypes


# In[6]:


df['book'] = pd.to_numeric(df['book']).astype(object)
df.dtypes


# # Books of the Bible Data

# ### Load and view file in dataframe

# In[7]:


df_books = pd.read_excel(
    '/Users/natha/Onedrive/Desktop/GitHub/personal/Data/bible_books.xlsx')

df_books.head(2)


# ### View and edit columns

# In[8]:


df_books.columns


# ### View and edit datatypes

# In[9]:


df_books.dtypes


# # Merge

# ### Left-joining Bible Verse Data with Books Data to create complete Bible database

# In[10]:


df_bible = pd.merge(df_books, df, on='book', how='left')
df_bible.head()


# ### Editing columns in new dataframe

# In[11]:


new_column_order = ['id', 'book', 'book_name', 'chapter', 'verse', 'text']

df_bible = df_bible[new_column_order]

print('Number of rows: ', df_bible.shape[0])
print('Number of columns: ', df_bible.shape[1])
df_bible.head()


# In[12]:


#df_bible = df_bible.set_index('id')

df_bible.to_csv(
    '/Users/natha/Onedrive/Desktop/GitHub/personal/Data/finished_bible.csv')


# In[13]:


df_bible.tail()


# In[14]:


range_low = 0


# In[15]:


range_high = 31102


# In[16]:


amount_of_variables = int(input('How many verses do you want? '))


# In[17]:


random_verse = random.sample(range(range_low, range_high), amount_of_variables)
print(
    df_bible.book_name.loc[random_verse].to_string(),
    df_bible.chapter.loc[random_verse].to_string(),
    df_bible.verse.loc[random_verse].to_string(),
    df_bible.text.loc[random_verse].to_string())
