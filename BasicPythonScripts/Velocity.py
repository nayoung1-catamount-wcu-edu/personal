print('Values are as follows: \nx = displacement: xi, xf','\nv = velocity: vi, vf','\nt = time','\na = acceleration')

equation = print(input('\nWhat value are you trying to find? '))

if equation == 'xi':
  print('Finding xi')
  value = 0
  while value == 0:
    try:
      xf = int(input('Enter a value for final displacement: '))
      vi = int(input('Enter value for initial velocity: '))
      vf = int(input('Enter value for final velocity: '))
      a = int(input('Enter value for acceleration: '))
      t = int(input('Enter a value for time: '))
      xi = (xf-(vi*t)-(0.5*(a)*(t**2)))
      xi2 = (xf-((vf-vi)/2)*t)
      print(xi == xi2, xi)
    except:
      print('Please enter a number. If you are solving for this variable, press "1".')

elif equation == 'xf':
  print('Finding xf')
  value = 0
  while value == 0:
    try:
      xi = int(input('Solve for initial displacement: '))
      vi = int(input('Enter value for initial velocity: '))
      vf = int(input('Enter value for final velocity: '))
      t = int(input('Enter a value for time: '))
      a = int(input('Enter value for acceleration: '))
      xf = (vi*t)+(0.5*a*(t**2))+xi
      xf2 = (((vf+vi)/2)*t)+xi
      xf == xf2
      print(xf == xf2)
    except:
      print('Please enter a number. If you are solving for this variable, press "1".')

elif equation == 'a':
  print('Finding a')
  value = 0
  while value == 0:
    try:
      vi = int(input('Enter value for initial velocity: '))
      vf = int(input('Enter value for final velocity: '))
      t = int(input('Enter a value for time: '))
      a = ((vf-vi)/t)
      print(a)
    except:
      print('Please enter a number. If you are solving for this variable, press "1".')
  

elif equation == 't':
  print('Finding t')
  value = 0
  while value == 0:
    try:
      vi = int(input('Enter value for initial velocity: '))
      vf = int(input('Enter value for final velocity: '))
      a = int(input('Enter value for acceleration: '))
      t = ((vf-vi)/a)
      print(t)
    except:
      print('Please enter a number. If you are solving for this varible, press "1".')
  

elif equation == 'vf':
  print('Finding vf')
elif equation == 'vi':
  print('Finding vi')



value = 0
while value == 0:
 try:
  vf = int(input('Enter value for final velocity: '))
  if vf >= 0 or vf < 0:
   value = 1
   break
 except:
  print('Please enter a number.')
  continue



value = 0
while value == 0:
 try:
  t = int(input('Enter a value for time: '))
  if t >= 0 or t < 0:
   value = 1
   break
 except:
  print('Please enter a number.')
  continue

#x = (vi*t) + (0.5*a*(t**2))

#(xf-xi) == ((0.5*(vf + vi))*t)
#(vf**2) == ((vi**2) + (2*a*(xf-xi)))
#vf == vi + (a*t)
#(xf-xi) == (vf*t - (0.5(a)(t**2)))"""