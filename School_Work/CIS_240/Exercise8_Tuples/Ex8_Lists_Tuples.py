graduates = ((1, "Hoshi Sato", 2019),
            (2, "John Doe", 2018),
            (3, "Amy Smith", 2018),
            (4, "Jane Smith", 2018),
            (5, "Alex John", 2018))

def getNameAndYearForGraduate(studentName):
    for graduate in graduates:
        if graduate[1] == studentName:
            return (graduate[1], graduate[2])

graduate = getNameAndYearForGraduate("Hoshi Sato")
print(graduate)