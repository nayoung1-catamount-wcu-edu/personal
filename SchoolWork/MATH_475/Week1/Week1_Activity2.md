# Week 1 Activity 2

There are many great tutorials on pandas for new users that go beyond what we have covered in the introductory videos.

Choose one of the tutorials listed [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)

Complete the tutorial, by reading/watching the video, taking notes, etc. You do not need to complete the entire tutorial, but you should spend at least 20 minutes gathering information in your preferred method.

In the space below, list three things that you learned from this tutorial.

List one way in which it differed from Dr. Penland's tutorial. (You do not have comment on better or worse, though it will not hurt my feelings if you do.)

--------------------------------------------------------------------------------

Tutorial: [Practical data analysis with Python](wavedatalab.github.io/datawithpython/)

Data Munging

- pd.cut(df[column], #categories)

  - somehow creates categories from data in the column

- df.ix[:,x:x]

  - follows a df.sort()
  - sorts column by cross-section of data

Data Aggregation

- pd.crosstab(df[column], df[column])

  - creates a crosstab of data by specified columns

- df.query()

  - creates a table based on the query entered

- df.groupby()

  - groups data by values in columns

Data Visualization

- pd.rolling_mean()

  - creates a moving average line
  - pd.stats.moments.rolling_mean()
