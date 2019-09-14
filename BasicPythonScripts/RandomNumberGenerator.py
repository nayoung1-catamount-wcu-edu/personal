#!/usr/bin/env python3.7

## This code is an attempt to use a random number generator to eventually create a 5 number summary.

# User input for the lowest value in a range.
enternumber = 0
  
while enternumber == 0:
  try:
    range_low = int(input("Lowest number of range: "))
    enternumber = 1
  except:
    print("Bummer. That broke. Please enter a numeric value.")

# User input for the highest value in a range.
enternumber = 0

while enternumber == 0:
  try:
    range_high = int(input("Highest number of range: "))
    enternumber = 1
  except:
    print("Bummer. That broke. Please enter a numeric value.")

# User input for how many variables to display
enternumber = 0

while enternumber == 0:
  try: 
    amount_of_variables = int(input("How many numbers do you want? "))
    enternumber = 1
  except:
    print("Bummer. That broke. Please enter a numeric value.")

# Using the stated range to find 15 random variables and add it to a list.
import random
random_list = random.sample(range(range_low,range_high), amount_of_variables)
print("Data has been successfully uploaded to randnumgen.txt.")

# Save results in txt doc
f=open('randnumgen.txt', 'a+')
f.write('%d,%d\n'%(range_low,range_high))
f.write("%s\n"%(random_list))
f.close()