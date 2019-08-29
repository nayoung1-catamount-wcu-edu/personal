import pandas as pd
import random

def runProgram():
 # Begin app
 input('Press a key to begin...')

 # Load dataframe
 df = pd.read_excel('/Users/natha/Onedrive/Desktop/personal/Data/finished_bible.xlsx')

 enternumber = 0
 while True:
 # Get a random verse
  n = random.randint(0,31102)
  n2 = n+1
  enternumber = 1

 # Print random verse
  print(df[n:n2])
  break

while True:
 runProgram()