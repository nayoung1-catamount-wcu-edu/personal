import random

def runProgram():
 input('Press Enter to run generator:')
 random_number = random.sample(range(1001001,1050026), 1)
 for number in random_number:
  print(number)

while True:
 runProgram()


## id format = bb/ccc/vvv