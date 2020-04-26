#!/usr/bin/env python3.7

# Imports
from spellchecker import SpellChecker

spell = SpellChecker()

## Kinematic Equations ##
print(
    "Values are as follows: \nd = displacement: d/x/yi, d/x/yf",
    "\nv = velocity: vi, vf",
    "\nt = time",
    "\na = acceleration",
)


def runProgram():
    equation = input("\nWhat value are you trying to find? ")

    # Initial displacement
    if equation == "xi" or equation == "yi" or equation == "di":
        print("Finding Initial Displacement")
        value = 0
        while value == 0:
            try:
                df = float(input("Enter a value for final displacement: "))
                vi = float(input("Enter value for initial velocity: "))
                vf = float(input("Enter value for final velocity: "))
                a = float(input("Enter value for acceleration: "))
                t = float(input("Enter a value for time: "))
                di = df - (vi * t) - (0.5 * (-a) * (t ** 2))
                print("\nInitial Displacement is: ", di)
                break
            except:
                break

    # Final displacement
    elif equation == "xf" or equation == "yf" or equation == "df":
        print("Finding Final Displacement")
        value = 0
        while value == 0:
            try:
                vi = float(input("Enter value for initial velocity: "))
                a = float(input("Enter value for acceleration: "))
                t = float(input("Enter a value for time: "))
                value = 1
                df = (vi * t) + (0.5 * (-a) * (t ** 2))
                print("\nFinal Displacement is: ", df)
                break
            except:
                break

    # Acceleration
    elif equation == "a":
        print("Finding Acceleration")
        value = 0
        while value == 0:
            try:
                d = float(input("Enter value for displacement: "))
                vi = float(input("Enter value for initial velocity: "))
                vf = float(input("Enter value for final velocity: "))
                # t = float(input('Enter a value for time: '))
                value = 1
                a = (vf ** 2 - vi ** 2) / (2 * d)
                print("\nAcceleration is: ", a)
                break
            except:
                break

    # Time
    elif equation == "t":
        print("Finding Time")
        value = 0
        while value == 0:
            try:
                d = float(input("Enter value for displacement: "))
                vi = float(input("Enter value for initial velocity: "))
                a = float(input("Enter value for acceleration: "))
                value = 1
                t = ((2 * d) / (-a)) ** 0.5
                print("\nTime is: ", t)
                break
            except:
                break

    # Final Velocity
    elif equation == "vf":
        print("Finding Final Velocity")
        value = 0
        while value == 0:
            try:
                d = float(input("Enter value for displacement: "))
                vi = float(input("Enter value for initial velocity: "))
                a = float(input("Enter value for acceleration: "))
                value = 1
                vf = (vi ** 2 + 2 * (-a) * d) ** 0.5
                print("\nFinal Velocity is: ", vf)
                break
            except:
                break

    # Initial Velocity
    elif equation == "vi":
        print("Finding Initial Velocity")
        value = 0
        while value == 0:
            try:
                d = float(input("Enter value for displacement: "))
                vf = float(input("Enter value for final velocity: "))
                a = float(input("Enter a value for acceleration: "))
                t = float(input("Enter value for time: "))
                value = 1
                vi = vf - (-a) * t
                print("\nInitial Velocity is: ", vi)
                break
            except:
                break

    ## End ##
    while True:
        print(
            "\nThanks for using this program. If you want to exit, enter 'yes'. If you would like to run the program again, enter 'no'."
        )
        val = input("Do you want to exit? ")
        if val == "yes":
            print("Goodbye!")
            import time

            time.sleep(2)
            exit()
        else:
            print("Resetting program...", "\n")
            import time

            time.sleep(2)
            break


while True:
    runProgram()
