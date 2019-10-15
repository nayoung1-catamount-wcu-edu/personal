classes = input('Enter the number of classes you are taking: ')
print(classes)

classHours = input('Enter number of hours for class: ')
print(classHours)

gpa = float(input('What is your grade in the class? '))

if gpa >= 90:
    print('Letter Grade: A')
elif gpa >= 80:
    print('Letter Grade: B')
elif gpa >= 70:
    print('Letter Grade: C')
elif gpa >= 60:
    print('Letter Grade: D')
else:
    print('Letter Grade: F')