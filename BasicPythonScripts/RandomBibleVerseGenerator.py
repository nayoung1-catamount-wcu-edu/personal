import pandas as pd
import random

input('Press a key to begin...')

df = pd.read_excel('/Users/owner/Onedrive/Desktop/personal/Data/finished_bible.xlsx')

#random_number = 1001001
n = random.randint(0,31102)
n2 = n+1

print(df[n:n2])