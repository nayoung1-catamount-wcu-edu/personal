import pandas as pd
import random

df = pd.read_excel('/Users/owner/Onedrive/Desktop/personal/Data/finished_bible.xlsx')

print(df['identifier'].head())

""" random_number = random.sample(range(1001001,1050026),1)

print(random_number)

def runProgram():
 for identifier in df_id:
  if identifier == random_number:
   print(identifier)

while True:
 runProgram() """