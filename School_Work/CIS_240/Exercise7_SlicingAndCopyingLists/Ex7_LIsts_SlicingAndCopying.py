#list of grades
myGrades = ["- A", "- B", "- B+", "- A-"]
suzyGreenbergGrades = myGrades[:]
#append grades
myGrades.append("- A+")
suzyGreenbergGrades.append("- C-")
#print functions
print("My grades are:")
for grade in myGrades:
    print(grade)

print("\nSuzy Greenberg's grades are:")
for grade in suzyGreenbergGrades:
    print(grade)