users = {
  'Bernard': {
    'username': 'Bernard',
    'securityQuestion': 'Is this a dream?',
    'securityAnswer': 'No.',
  },
  'Charlotte': { 
    'username': 'Charlotte',
    'securityQuestion': 'What is your favorite color?',
    'securityAnswer': 'Purple.',
  },
  'Teddy' : {  
    'username': 'Teddy',
    'securityQuestion': 'In which city were you born?',
    'securityAnswer': 'Cullowhee',
  }

for key, value in users.items():
  username = value['username']
  securityQuestion = value['securityQuestion']
  answer = value['securityAnswer'] 

  print('\nusername: ' + username)
  print('security question: ' + securityQuestion)
  print('Security Answer: ' + securityAnswer)