grades = []

class Grade:
  def __init__(self, gradeID, grade, exerciseName , exerciseDueDate):
    self.gradeID = gradeID
    self.grade = grade
    self.exerciseName = exerciseName
    self.exerciseDueDate = exerciseDueDate
    grades.append(self)