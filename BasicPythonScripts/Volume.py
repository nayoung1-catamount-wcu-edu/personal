## Imports ##
from spellchecker import SpellChecker
import math
spell = SpellChecker()

## Volume ##
def runProgram():
  print('Hello! This program will help you find volumes for different shapes.')
  find_shape = spell.candidates(input('What shape do you want to find an volume for? '))
  
  for shape in find_shape:
    if (shape == 'cube' or \
      shape == 'rectangular' or \
      shape == 'parallelogram' or \
      shape == 'cone' or \
      shape == 'cylinder' or \
      shape == 'triangular' or \
      shape == 'pyramid'):
        find_shape = shape
    else:
      shape = 'none'



## cube ##
  if find_shape == 'cube':
    print('\nFinding Volume of a Cube')

    # Enter sideA
    number = 0
    while number == 0:
      try:
        sideA = int(input('Enter a value for sideA: '))
        if sideA > 0:
          number = 1
        else:
          number = 0
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

      # Print volume of cube
      cube = sideA**3
      print('Volume of cube: ',cube,'\n')



## rectangluar prism ##
  elif find_shape == 'rectangular':
    print('\n')
    print('Finding Volume of a Rectangluar Prism')

    # Enter sideA
    number = 0
    while number == 0:
      try:
        sideA = int(input('Enter a value for side A: '))
        if sideA > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter sideB
    number = 0
    while number == 0:
      try:
        sideB = int(input('Enter a value for side B: '))
        if sideB > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter sideC
    number = 0
    while number == 0:
      try:
        sideC = int(input('Enter a value for sideC: '))
        if sideC > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue
        
    # Print volume of rectangluar prism
    rectangluarPrism = sideA*sideB*sideC
    print('Volume of rectangluar prism: ',rectangluarPrism,'\n')



## Sphere ##
  elif find_shape == 'sphere':
    print('\n')
    print('Finding Volume of a Sphere')

    # Enter radius
    number = 0
    while number == 0:
      try:
        radius = int(input('Enter a value for length: '))
        if radius > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print volume of a sphere
    sphere = (4/3)*(math.pi)*(radius**3)
    print('Volume of parallelogram: ',sphere,'\n')



## cone ##
  elif find_shape == 'cone':
    print('\n')
    print('Finding Volume of a Cone')

    # Enter height
    number = 0
    while number == 0:
      try:
        height = int(input('Enter a value for height: '))
        if height > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter r
    number = 0
    while number == 0:
      try:
        r = int(input('Enter a value for r: '))
        if r > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print volume of cone
    cone = (1/3)*(math.pi)*(r**2)*(height)
    print('Volume of cone: ',cone,'\n')



## cylinder ##
  elif find_shape == 'cylinder':
    print('\n')
    print('Finding Volume of a Cylinder')
    math.pi

    # Enter r
    number = 0
    while number == 0:
      try:
        r = int(input('Enter a value for r: '))
        if r > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter height
    number = 0
    while number == 0:
      try:
        height = int(input('Enter a value for height: '))
        if height > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print volume of cylinder
    cylinder = (math.pi)*(r**2)*(height)
    print('Volume of cylinder: ',cylinder,'\n')



## triangular prism ##
  elif find_shape == 'triangular':
    print('\n')
    print('Finding Volume of a Triangular Prism')

    # Enter length
    number = 0
    while number == 0:
      try:
        length = int(input('Enter a value for length: '))
        if length > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter width
    number = 0
    while number == 0:
      try:
        width = int(input('Enter a value for width: '))
        if width > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter hight
    number = 0
    while number == 0:
      try:
        height = int(input('Enter a value for height: '))
        if height> 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print volume of triangular prism
    triangularPrism = (0.5)*(length)*(width)*(height)
    print('Volume of triangular prism: ',triangularPrism,'\n')



## pyramid ##
  elif find_shape == 'pyramid':
    print('\n')
    print('Finding Volume of a Pyramid')

    # Enter base
    number = 0
    while number == 0:
      try:
        base = int(input('Enter a value for base: '))
        if base > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter height
    number = 0
    while number == 0:
      try:
        height = int(input('Enter a value for height: '))
        if height > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print volume of equlateral triangular prism
    pyramid = (1/3)*(base)*(height)
    print('Volume of pyramid: ',pyramid,'\n')



## Other ##
  else:
    print('Unfortunately, this program cannot find the volume for that shape.')

  while True:
    print("Thanks for using this program. If you want to exit, enter 'yes'.  If you would like to run the program again, enter 'no'.")
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