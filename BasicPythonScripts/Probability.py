import statistics
from tabulate import tabulate
import numpy as np
import math

# Random Variable Mean
def random_mean():
    x = [
        float(x) for x in input("Enter all values for x, separated by spaces: ").split()
    ]

    # Calculate Mean
    mean = statistics.mean(x)
    print("\nMean of", x, "is:", round(mean, 4))

    # Calculate Std Dev
    std_dev = statistics.stdev(x)
    print("\nStandard Deviation of", x, "is:", round(std_dev, 4))

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
        round(mean, 4),
        "\nStandard Deviation: ",
        round(sigma, 4),
        "\n",
        sep="",
    )

    while True:
        exit()


# Binomial Distribution
def binomial_distribution():
    # n = number of trials
    n = int(input("Enter number of trials: "))

    # x = number of successes
    x = int(input("Enter number of successes: "))

    # p = probability as decimal
    p = float(input("Enter probability as a decimal: "))

    # Pr = what we are solving for
    Pr = (
        (math.factorial(n) / (math.factorial(x) * (math.factorial(n - x))))
        * (p ** x)
        * ((1 - p) ** (n - x))
    )

    print("\nProbability of", x, "successes from", n, "trials is:", round(Pr, 4))


# Normal Distributions
def normal_distribution():
    x = int(input("\nWhat value are you solving for? "))
    mean = int(input("Enter mean: "))
    std_dev = int(input("Enter std dev: "))

    # z score
    z = (x - mean) / std_dev
    if z >= 0:
        print("\nPostitive z-score of:", round(z, 4))
    else:
        print("\nNegative z-score of:", round(z, 4))


# Program
try:
    problem = int(input("What type of problem are you solving? "))
    if problem == 1:
        random_mean()
    elif problem == 2:
        probability_distribution()
    elif problem == 3:
        binomial_distribution()
    elif problem == 4:
        normal_distribution()
    else:
        exit()

# Error catching
except statistics.StatisticsError:
    print("\nPlease enter at least 2 values.\n")

except ValueError:
    print("\nThat did not work.  Please enter a numerical value.\n")
