# Imports


```python
import pandas as pd
```

# Read Data


```python
# Read and display csv data
impeach_df = pd.read_csv("impeach.csv")
impeach_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Senator</th>
      <th>State</th>
      <th>Article1</th>
      <th>Article2</th>
      <th>Guilt</th>
      <th>Party</th>
      <th>Conservatism</th>
      <th>Clinton</th>
      <th>Reelection</th>
      <th>FirstTerm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>shelby</td>
      <td>AL</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>92</td>
      <td>43</td>
      <td>2004</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sessions</td>
      <td>AL</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>100</td>
      <td>43</td>
      <td>2002</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>murkowsk</td>
      <td>AK</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>68</td>
      <td>34</td>
      <td>2004</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>stevens</td>
      <td>AK</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>58</td>
      <td>34</td>
      <td>2002</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>kyl</td>
      <td>AZ</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>96</td>
      <td>47</td>
      <td>2000</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



# Questions

### What state did Daniel Patrick Moynahan represent?


```python
# Set index as Senator
impeach_df.index = impeach_df["Senator"]
```


```python
# Search index for Moynihan
impeach_df.loc["moynihan"]
```




    Senator         moynihan
    State                 NY
    Article1               0
    Article2               0
    Guilt                  0
    Party                  0
    Conservatism          12
    Clinton               59
    Reelection          2000
    FirstTerm              0
    Name: moynihan, dtype: object




```python
# Answer
print("Daniel Patrick Moynihan represented NY.")
```

    Daniel Patrick Moynihan represented NY.
    

### What was the standard deviation of the conservatism score for senators in 1998? (Hint: use the "std" command to get the standard deviation.) 


```python
# Separate conservatism scores from original dataframe
conservatism_score = impeach_df["Conservatism"]

# Get the standard deviation of the newly created dataframe
std_conservatism = conservatism_score.std()

# Answer
print("The standard deviation of Conservatism score was " + str(std_conservatism))
```

    The standard deviation of Conservatism score was 37.477992195285736
    

### Which of Tennesse's two senators was ranked as more conservative in 1998: Thompson or Graham?


```python
# Get information on Thompson
impeach_df.loc["thompson"]
```




    Senator         thompson
    State                 TN
    Article1               0
    Article2               1
    Guilt                  1
    Party                  1
    Conservatism          88
    Clinton               48
    Reelection          2002
    FirstTerm              1
    Name: thompson, dtype: object




```python
# Get information on Graham
impeach_df.loc["graham"]
```




    Senator         graham
    State               FL
    Article1             0
    Article2             0
    Guilt                0
    Party                0
    Conservatism         8
    Clinton             48
    Reelection        2004
    FirstTerm            0
    Name: graham, dtype: object




```python
# Answer
print("The Tennesse senator who ranked more conservative in 1998 was Senator Thompson with a Conservatism score of 88.")
```

    The Tennesse senator who ranked more conservative in 1998 was Senator Thompson with a Conservatism score of 88.
    

### What percentage of the vote did Bill Clinton receive in New York in the 1996 election?


```python
# Filter dataframe to show only NY
ny_filter = impeach_df["State"] == "NY"
impeach_df = impeach_df[ny_filter]
print(impeach_df)
```

               Senator State  Article1  Article2  Guilt  Party  Conservatism  \
    Senator                                                                    
    moynihan  moynihan    NY         0         0      0      0            12   
    schumer    schumer    NY         0         0      0      0            19   
    
              Clinton  Reelection  FirstTerm  
    Senator                                   
    moynihan       59        2000          0  
    schumer        59        2004          1  
    


```python
# Answer
print("The percentage of votes Bill Clinton received in New York was 59%.") 
```

    The percentage of votes Bill Clinton received in New York was 59%.
    

### **Bonus**: Senator Kay Bailey Hutchison is not coded as "hutchison". Using any method, find the row that corresponds to Kay Bailey Hutchinson. Describe the method you used. 


```python
# Load a clean dataframe
impeach_df = pd.read_csv("impeach.csv")
```


```python
# Filter the dataframe to only show rows matching the senator name found above
kbh_filter = impeach_df["Senator"] == "kaybhut"
impeach_df = impeach_df[kbh_filter]

# print the dataframe to show the row
impeach_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Senator</th>
      <th>State</th>
      <th>Article1</th>
      <th>Article2</th>
      <th>Guilt</th>
      <th>Party</th>
      <th>Conservatism</th>
      <th>Clinton</th>
      <th>Reelection</th>
      <th>FirstTerm</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>85</th>
      <td>kaybhut</td>
      <td>TX</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>92</td>
      <td>44</td>
      <td>2000</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Answer
print("Senator Kay Bailey Hutchinson can be found under the name of 'kaybhut' in row 85.")
```

    Senator Kay Bailey Hutchinson can be found under the name of 'kaybhut' in row 85.
    
