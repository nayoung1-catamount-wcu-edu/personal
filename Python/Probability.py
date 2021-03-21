import statistics
from tabulate import tabulate
import numpy as np
import math
import scipy.stats as st
from scipy.integrate import quad
import os
import time


# Program

try:

    def runProgram():
        clear()
        problem = int(
            input(
                "What type of problem are you solving?\n\nList:\n1 Event Probabilty\n2 Random Mean\n3 Probability Distribution\n4 Binomial Distribution\n5 Normal Distribution\n6 Sample Mean\n7 Sample Proportion\n\n"
            )
        )
        if problem == 1:
            clear()
            print("\nSolving Event Probability")
            event_probability()
        elif problem == 2:
            clear()
            print("\nSolving for Random Mean")
            random_mean()
        elif problem == 3:
            clear()
            print("\nSolving for probability distribution.")
            probability_distribution()
        elif problem == 4:
            clear()
            print("\nSolving for binomial distribution.")
            binomial_distribution()
        elif problem == 5:
            clear()
            print("\nSolving for normal distribution.")
            normal_distribution()
        elif problem == 6:
            clear()
            print("\nSolving for sample mean.")
            sample_mean()
        elif problem == 7:
            clear()
            print("\nSolving for sample proportion.")
            sample_proportion()
        else:
            exit()

    while True:
        runProgram()

# Error catching
except statistics.StatisticsError:
    print("\nPlease enter at least 2 values.\n")

except ValueError:
    print("\nThat did not work.  Please enter a numerical value.\n")


# Clear terminal
def clear():
    os.system("cls")


# Event probability
def event_probability():
    options = int(
        input("\nMenu:\n1 Single Event\n2 Multi Event\nWhat are you solving for? ")
    )
    if options == 1:
        n = int(input("\nNumber of possible outcomes: "))
        x = int(input("Number of events occured: "))
        pa = n / x
        pa_ = 1 - pa
        print("\nP(A):", pa, "\nP(~A):", pa_)
    elif options == 2:
        n = int(input("Number of possible outcomes: "))
        a = int(input("Number of events occured in event A: "))
        b = int(input("Number of events occured in event B: "))
        pa = a / n
        pa_ = 1 - pa
        pb = b / n
        pb_ = 1 - pb
        both = pa * pb
        either = pa + pb - both
        conditional = both / pb
        print(
            "\nP(A):",
            round(pa, 4),
            "\nP(~A):",
            round(pa_, 4),
            "\nP(B):",
            round(pb, 4),
            "\nP(~B):",
            round(pb_, 4),
            "\nP(A n B):",
            round(both, 4),
            "\nP(A U B):",
            round(either, 4),
            "\nP(A|B):",
            round(conditional, 4),
        )
    else:
        print("Please enter a value from the menu.")
        event_probability()

    while True:
        time.sleep(15)
        runProgram()


# Random Variable Mean
def random_mean():
    x = [
        float(x) for x in input("Enter all values for x, separated by spaces: ").split()
    ]

    # Calculate Mean
    mean = statistics.mean(x)
    print("\nMean of", x, "is:", round(mean, 10))

    # Calculate Std Dev
    std_dev = statistics.stdev(x)
    print("\nStandard Deviation of", x, "is:", round(std_dev, 10))

    while True:
        exit()


# Probablility Distribution
def probability_distribution():
    # x values
    x = [
        float(x) for x in input("Enter all values for x, separated by spaces: ").split()
    ]

    # P(x) values
    px = [
        float(px)
        for px in input("Enter all values for P(x), separated by spaces: ").split()
    ]

    # Calculate mean
    mean = sum([x * px for x, px in zip(x, px)])

    # Calculate std dev
    # a = (x-mean)**2
    # b = a*px
    # sigma = sqrt(sum(b))
    a = [(x[i] - mean) ** 2 for i in range(len(x))]

    b = [a[i] * px[i] for i in range(len(px))]

    sigma = np.sqrt(sum(b))

    # print(std_dev)
    print(
        "\n",
        (tabulate([["x", x], ["P(x)", px]], tablefmt="fancy_grid")),
        "\n\nMean: ",
        round(mean, 10),
        "\nStandard Deviation: ",
        round(sigma, 10),
        "\n",
        sep="",
    )

    while True:
        exit()


# Binomial Distribution
def binomial_distribution():
    # n = number of trials
    n = int(input("Enter n, numer of trials: "))

    # x = number of successes
    x = int(input("Enter x, number of successes: "))

    # p = probability as decimal
    p = float(input("Enter p as a decimal: "))

    # Pr = what we are solving for
    Pr = (
        (math.factorial(n) / (math.factorial(x) * (math.factorial(n - x))))
        * (p ** x)
        * ((1 - p) ** (n - x))
    )

    print("\nProbability of", x, "successes from",
          n, "trials is:", round(Pr, 10))


# Normal Distributions
def normal_distribution():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import norm

    x = float(input("\nWhat value are you solving for? "))
    mean = float(input("Enter mean: "))
    std_dev = float(input("Enter std dev: "))

    # z score
    z = (x - mean) / std_dev
    if z >= 0:
        print("\nPostitive z-score of:", round(z, 10))
    else:
        print("\nNegative z-score of:", round(z, 10))

    def draw_z_score(x, cond, mean, std_dev, title):
        y = norm.pdf(x, mean, std_dev)
        z = x[cond]
        plt.plot(x, y)
        plt.fill_between(z, 0, norm.pdf(z, mean, std_dev))
        plt.title(title)
        plt.show()

    # probability
    def normalProbabilityDensity(x):
        constant = 1.0 / np.sqrt(2 * np.pi)
        return constant * np.exp((-(x ** 2)) / 2.0)


# Sampling Mean
def sample_mean():
    # Sample Size
    n = float(input("\nEnter sample size: "))

    # Population mean
    x = float(input("Enter population mean: "))

    # Observation Mean
    x_bar = float(input("Enter observation mean: "))

    # Standard Deviation
    std_dev = float(input("Enter population standard deviation: "))

    # Sample Population Std Dev
    std_dev_x = std_dev / np.sqrt(n)

    # z score
    z = (x_bar - x) / std_dev_x

    print("\nPopulation Std Dev: ", std_dev_x, "\nZ-Score: ", z)


# Sampling Proportion
def sample_proportion():
    # Population proportion
    p = float(input("\nEnter the sample proportion: "))

    # Number of trials
    n = float(input("Enter the number of samples: "))

    # Standard Deviation
    a = p * (1 - p)
    b = a / n
    std_dev = np.sqrt(b)

    distribution = n * p
    if distribution >= 10 and n * (1 - p) >= 10:
        print("\nThis distribution is approximately normal.")
    else:
        print("\nThis distribution is not approximately normal.")

    # Z score
    p_hat = float(input("\nEnter value for p-hat: "))
    z = (p_hat - p) / std_dev

    print(
        "\nPopulation Proportion Mean: ",
        round(p, 10),
        "\nPopulation Standard Deviation: ",
        round(std_dev, 10),
        "\nProbability: ",
        round(z, 10),
    )
