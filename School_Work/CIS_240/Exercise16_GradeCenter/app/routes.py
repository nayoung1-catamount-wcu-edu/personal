from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', pageheader="All Grades")
  #student = {'name': 'Harpua', 'major': 'CIS', 'id': '92012345'}
  #return '''
#<html>
  #<head>
   # <title>Student Roster</title>
  #</head>
  #<body>
  #  <h1>''' +student['name'] + '''</h1>
   # <h2>Major: ''' + student['major'] + '''</h2>
   # <h2>920#: ''' + student['id'] + '''</h2>
  #</body>
#</html> '''