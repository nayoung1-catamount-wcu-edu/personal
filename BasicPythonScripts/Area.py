#!/usr/bin/env python3.7

## Imports ##
from spellchecker import SpellChecker
import math
spell = SpellChecker()

## Area ##
def runProgram():
  print('Hello! This program will help you find areas for different shapes.')
  find_shape = spell.candidates(input('What shape do you want to find an area for? '))
  
  for shape in find_shape:
    if (shape == 'square' or \
      shape == 'rectangle' or \
      shape == 'parallelogram' or \
      shape == 'trapezoid' or \
      shape == 'circle' or \
      shape == 'triangle' or \
      shape == 'equilateral triangle' or \
      shape == 'ellipse'):
        find_shape = shape
    else:
      shape = 'none'


  ## Square ##
  if find_shape == 'square':
    print('\nFinding Area of a Square')

    # Enter base/height
    number = 0
    while number == 0:
      try:
        side = float(input('Enter a value for a side: '))
        if side > 0:
          number = 1
        else:
          number = 0
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

      # Print area of square
      square = side**2
      print('Area of square: ',square,'\n')

  ## Rectangle ##
  elif find_shape == 'rectangle':
    print('\n')
    print('Finding Area of a Rectangle')

    # Enter length
    number = 0
    while number == 0:
      try:
        length = float(input('Enter a value for length: '))
        if length > 0:
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
        height = float(input('Enter a value for height: '))
        if height > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of rectangle
    rectangle = length*height
    print('Area of rectangle: ',rectangle,'\n')


  ## Parallelogram ##
  elif find_shape == 'parallelogram':
    print('\n')
    print('Finding Area of a Parallelogram')

    # Enter length
    number = 0
    while number == 0:
      try:
        length = float(input('Enter a value for length: '))
        if length > 0:
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
        height = float(input('Enter a value for height: '))
        if height > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of parallelogram
    parallelogram = length * height
    print('Area of parallelogram: ',parallelogram,'\n')


  ## Trapezoid ##
  elif find_shape == 'trapezoid':
    print('\n')
    print('Finding Area of a Trapezoid')

    # Enter height
    number = 0
    while number == 0:
      try:
        height = float(input('Enter a value for height: '))
        if height > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter b1
    number = 0
    while number == 0:
      try:
        b1 = float(input('Enter a value for b1: '))
        if b1 > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter b2
    number = 0
    while number == 0:
      try:
        b2 = float(input('Enter value for b2: '))
        if b2 > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of trapezoid
    trapezoid = ((height)/2)*(b1 + b2)
    print('Area of trapezoid: ',trapezoid,'\n')


  ## Circle ##
  elif find_shape == 'circle':
    print('\n')
    print('Finding Area of a Circle')
    math.pi

    # Enter r
    number = 0
    while number == 0:
      try:
        r = float(input('Enter a value for r: '))
        if r > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of circle
    circle = math.pi*(r**2)
    print('Area of circle: ',circle,'\n')


  ## Ellipse ##
  elif find_shape == 'ellipse':
    print('\n')
    print('Finding Area of an Ellipse')
    math.pi

    # Enter r1
    number = 0
    while number == 0:
      try:
        r_1 = float(input('Enter a value for r1: '))
        if r_1 > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Enter r2
    number = 0
    while number == 0:
      try:
        r_2 = float(input('Enter a value for r2: '))
        if r_2 > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of ellipse
    ellipse = math.pi*(r_1*r_2)
    print('Area of ellipse: ',ellipse,'\n')


  ## Triangle ##
  elif find_shape == 'triangle':
    print('\n')
    print('Finding Area of a Triangle')

    # Enter base
    number = 0
    while number == 0:
      try:
        base = float(input('Enter a value for length: '))
        if base> 0:
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
        height = float(input('Enter a value for height: '))
        if height> 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of triangle
    triangle = (0.5)*(base)*(height)
    print('Area of triangle: ',triangle,'\n')


  ## Equilateral Triangle ##
  elif find_shape == 'equilateral triangle':
    print('\n')
    print('Finding Area of an Equilateral Triangle')

    # Enter side_a
    number = 0
    while number == 0:
      try:
        side_a = float(input('Enter a value for length: '))
        if side_a > 0:
          number = 1
        else:
          print('Value cannot be less than or equal to 0.')
      except:
        print('Please enter a numeric value.')
        continue

    # Print area of equlateral triangle
    eq_triangle = ((3**0.5)/4)*(side_a**2)
    print('Area of equilateral triangle: ',eq_triangle,'\n')


  ## End ##
  else:
    print('Unfortunately, this program cannot find the area for that shape.')

  while True:
    print("Thanks for using this program. If you want to exit, enter 'yes'.  If you would like to run the program again, enter 'no'.")
    val = spell.candidates(input('Do you want to exit? '))
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