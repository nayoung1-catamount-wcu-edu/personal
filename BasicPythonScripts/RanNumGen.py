import numpy as np
import time

def runProgram():
 number = 0
 while number == 0:
  try:
   x = np.random.randint(1,100,10)
   print(x)
   number = 1
  except:
   continue
   time.sleep(2)

while True:
 runProgram()