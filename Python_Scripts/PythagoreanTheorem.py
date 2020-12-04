#!/usr/bin/env python3.9

## Pythagorean Theorem ##
def runProgram():
    print("Solver for Pythagorean Theorem", "\n")

    # Enter sideA
    number = 0
    while number == 0:
        try:
            variable_a = float(input("Enter a value for side a: "))
            number = 1
        except BaseException:
            print("Please enter a numeric value.")

    # Enter sideB
    number = 0
    while number == 0:
        try:
            variable_b = float(input("Enter a value for side b: "))
            number = 1
        except BaseException:
            print("Please enter a numeric value.")

    if variable_b <= 0:
        print("Cannot use values less than 1.")

    # Solve for sideC
    theorem = (variable_a ** 2 + variable_b ** 2) ** 0.5
    print("Side c is: ", theorem)

    print("Thanks for using this program!")
    import time

    time.sleep(2)

    # Exit or rerun program
    print("Enter 'yes' for exit, 'no' to run the program again.")
    val = input("Do you want to exit? ")
    # Exit
    while True:
        if val == "yes":
            print("Goodbye!")
            import time

            time.sleep(2)
            exit(0)
        # Rerun
        elif val == "no":
            print("Resetting program...", "\n")
            import time

            time.sleep(2)
            break


# If answer to previous question is yes, resume program
while True:
    runProgram()
