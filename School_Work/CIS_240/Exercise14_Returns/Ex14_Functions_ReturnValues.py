def gradeCenter(exerciseName, score, exerciseID, **kwargs):
  wcuStudent = {"Name":exerciseName, "Score" :score, "id": exerciseID}
  for key, pair in kwargs.items():
    wcuStudent[key]= pair
  return wcuStudent

wcuStudent = gradeCenter("Functions-ReturnValues", 100, 14, completed=True)
print(wcuStudent)