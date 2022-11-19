from flask import render_template, redirect, url_for, request
from app import app
from grade import Grade

grades = []

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    newGradeID = request.form.get("gradeID", "")
    newGrade = request.form.get("grade", "")
    newExerciseName = request.form.get("exerciseName", "")
    newExerciseDueDate = request.form.get("exerciseDueDate", "")

    newGrade = Grade(gradeID=newGradeID, grade=newGrade, exerciseName=newExerciseName, exerciseDueDate=newExerciseDueDate)
    grades.append(newGrade)
    return redirect(url_for("index"))
  return render_template("index.html", pageheader="All Grades", grades=grades)