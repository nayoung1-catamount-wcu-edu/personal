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
   shape == 'circle' or \
   shape == 'triangle'):
   find_shape = shape
  else:
   shape = 'none'

 if find_shape == 'square' or find_shape == 'rectangle' or find_shape == 'parallelogram':
  length = int(input('Enter length: '))
  width = int(input('Enter width: '))
  perimeter = 2*(length + width)
  print('Perimeter for',find_shape,'is: ',perimeter)

 if find_shape == 'triangle':
  sideA = int(input('Enter side a: '))
  sideB = int(input('Enter side b: '))
  sideC = int(input('Enter side c: '))
  perimeter = sideA + sideB + sideC
  print('Perimeter is: ',perimeter)

 if find_shape == 'circle':
  r = int(input('Enter radius: '))
  d = 2*r
  C = math.pi*d
  print('Circumference is: ',C)

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