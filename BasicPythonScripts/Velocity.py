print('Values are as follows: \nx = displacement: xi, xf','\nv = velocity: vi, vf','\nt = time','\na = acceleration')

equation = print(input('\nWhat value are you trying to find? '))
if equation == 'xi':
 print('')
elif equation == 'xf':
 print('')
elif equation == 'a':
 print('')
elif equation == 't':
 print('')
elif equation == 'vf':
 print('')
elif equation == 'vi':
 print('')

value = 0
while value == 0:
 try:
  xi = int(input('Enter value for initial displacement: '))
  if xi >= 0 or xi < 0:
   value = 1
   break
 except:
  print('Please enter a number. If you are solving for this variable, press "1".')
  continue

value = 0
while value == 0:
 try:
  xf = int(input('Enter value for final displacement: '))
  if xf >= 0 or xf < 0:
   value = 1
   break
 except:
  print('Please enter a number.')
  continue

value = 0
while value == 0:
 try:
  vi = int(input('Enter value for initial velocity: '))
  if vi >= 0 or vi < 0:
   value = 1
   break
 except:
  print('Please enter a number.')
  continue

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
  a = int(input('Enter value for acceleration: '))
  if a >= 0 or xf < 0:
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
#(xf-xi) == (vf*t - (0.5(a)(t**2)))