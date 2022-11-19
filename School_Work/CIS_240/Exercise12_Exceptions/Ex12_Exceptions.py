users = {
  'Bernard': {
    'username': 'Bernard',
    'securityQuestion': 'Is this a dream?',
    'securityAnswer': 'No',
  },
  'Charlotte': { 
    'username': 'Charlotte',
    'securityQuestion': 'What is your favorite color?',
    'securityAnswer': 'Purple',
  },
  'Teddy' : {  
    'username': 'Teddy',
    'securityQuestion': 'In which city were you born?',
    'securityAnswer': 'Cullowhee',
  }
} 

for key, value in users.items():
  username = value ['username']
  securityQuestion = value ['securityQuestion']
  securityAnswer = value ['securityAnswer'] 

  print('\nUsername: ' + username)
  print('Security question: ' + securityQuestion)
  print('Security answer: ' + securityAnswer)

  try:
    emailAddress = users['emailAddress']
  except KeyError:
    print('Error finding emailAddress')

  try:
    userName = users + [920637657]
  except TypeError:
    print("These two data types can't be added together!")