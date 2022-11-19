##First Function-gradeCenter
def gradeCenter(excerciseName, grade):
  print("\nExercise Name: " + excerciseName)
  print("Score: " + grade)

gradeCenter("Functions.", "100")

##Second Function-gradeCenterKwargs
def gradeCenterKwargs(excerciseName, grade):
  print("\nExercise Name: " + excerciseName)
  print("Score: " + grade)

gradeCenterKwargs(excerciseName="Functions.", grade="100")

##Third Function-gradeCenterVarargs
def gradeCenterVarargs(excerciseName, **kwargs):
  print("\nExercise Name: " + excerciseName)
  print("Score: " + kwargs["grade"])
  print("Excercise ID: " + kwargs["excerciseID"])

gradeCenterVarargs(excerciseName="Function", grade="100", excerciseID="13")