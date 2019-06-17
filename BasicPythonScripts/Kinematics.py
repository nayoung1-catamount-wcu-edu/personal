print('Values are as follows: \nd = displacement: d/x/yi, d/x/yf','\nv = velocity: vi, vf','\nt = time','\na = acceleration')

def runProgram():
  equation = (input('\nWhat value are you trying to find? '))

  if equation == 'xi' or equation == 'yi' or equation == 'di':
    print('Finding Initial Displacement')
    value = 0
    while value == 0:
      try:
        df = float(input('Enter a value for final displacement: '))
        vi = float(input('Enter value for initial velocity: '))
        vf = float(input('Enter value for final velocity: '))
        a = float(input('Enter value for acceleration: '))
        t = float(input('Enter a value for time: '))
        di = (xf-(vi*t)-(0.5*(-a)*(t**2)))
        di2 = (xf-((vf-vi)/2)*t)
        print(di == di2, di)
      except:
        break


  elif equation == 'xf' or equation == 'yf' or equation == 'df':
    print('Finding Final Displacement')
    value = 0
    while value == 0:
      try:
        di = float(input('Solve for initial displacement: '))
        vi = float(input('Enter value for initial velocity: '))
        vf = float(input('Enter value for final velocity: '))
        t = float(input('Enter a value for time: '))
        a = float(input('Enter value for acceleration: '))
        df = (vi*t)+(0.5*(-a)*(t**2))+di
        df2 = (((vf+vi)/2)*t)+di
        df == df2
        print(df == df2)
      except:
        break


  elif equation == 'a':
    print('Finding Acceleration')
    value = 0
    while value == 0:
      try:
        vi = float(input('Enter value for initial velocity: '))
        vf = float(input('Enter value for final velocity: '))
        t = float(input('Enter a value for time: '))
        a = ((vf-vi)/t)
        print(a)
      except:
        break
    

  elif equation == 't':
    print('Finding Time')
    value = 0
    while value == 0:
      try:
        d = float(input('Enter value for displacement: '))
        vi = float(input('Enter value for initial velocity: '))
        vf = float(input('Enter value for final velocity: '))
        a = float(input('Enter value for acceleration: '))
        t = (((2*d)/a)**0.5)
        print(t)
      except:
        break
    

  elif equation == 'vf':
    print('Finding Final Velocity')
    value = 0
    while value == 0:
      try:
        vi = float(input('Enter value for initial velocity: '))
        a = -9.8
        t = float(input('Enter a value for time: '))
        vf = vi + a*t
        print(vf)
      except:
        break


  elif equation == 'vi':
    print('Finding Initial Velocity')
    value = 0
    while value == 0:
      try:
        vf = float(input('Enter value for final velocity: '))
        a = -9.8
        t = float(input('Enter a value for time: '))
        vf = vi + a*t
        print(vi)
      except:
        break

while True:
  runProgram()