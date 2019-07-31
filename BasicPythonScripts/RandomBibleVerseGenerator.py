import pandas as pd
import random

# Begin app
input('Press a key to begin...')

# Load dataframe
df = pd.read_excel('/Users/owner/Onedrive/Desktop/personal/Data/finished_bible.xlsx')

# Get a random verse
n = random.randint(0,31102)
n2 = n+1

# Print random verse
print(df[n:n2])