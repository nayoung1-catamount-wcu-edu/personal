from spellchecker import SpellChecker
import math
spell = SpellChecker()

def runProgram():
 find_shape = spell.candidates(input('What shape do you want to find perimeter for? '))

 for shape in find_shape:
  if (shape == 'square' or \
   shape == 'rectangle' or \
   shape == 'parallelogram' or \
   shape == 'trapezoid' or \
   shape == 'irregular' or \
   shape == 'circle' or \
   shape == 'triangle'):
   find_shape = shape
  else:
   shape = 'none'

 if find_shape == 'square' or find_shape == 'rectangle' or find_shape == 'parallelogram':
  length = float(input('Enter length: '))
  width = float(input('Enter width: '))
  perimeter = 2*(length + width)
  print('Perimeter for',find_shape,'is: ',perimeter)

 if find_shape == 'triangle':
  sideA = float(input('Enter side a: '))
  sideB = float(input('Enter side b: '))
  sideC = float(input('Enter side c: '))
  perimeter = sideA + sideB + sideC
  print('Perimeter is: ',perimeter)

 if find_shape == 'circle':
  r = float(input('Enter radius: '))
  d = 2*r
  C = math.pi*d
  print('Circumference is: ',C)

 if find_shape == 'trapezoid':
  a = float(input('Enter side 1: '))
  b1 = float(input('Enter side 2: '))
  b2 = float(input('Enter side 3: '))
  c = float(input('Enter side 4:'))
  p = a + b1 + b2 + c
  print('Perimeter for',find_shape,'is :',p)

 if find_shape == 'irregular':
  sides = float(input('How many sides are there: '))
  s1 = float(input('Enter side: '))
  value = 0
  while value == 0:
   s = s1 + 1
   s = (s1 + 1)
   value = 1
   p = s
   print(p)

 while True:
   print("\nThanks for using this program. If you want to exit, enter 'yes'.  If you would like to run the program again, enter 'no'.")
   val = (input('Do you want to exit? '))
   if val == 'yes':
     print('Goodbye!')
     import time
     time.sleep(2)
     exit(0)
   else:
     print('Resetting program...','\n')
     import time
     time.sleep(2)
     break

while True:
 runProgram()