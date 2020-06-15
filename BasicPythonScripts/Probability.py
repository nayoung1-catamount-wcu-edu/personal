import statistics
from tabulate import tabulate
import numpy as np

# Random Variable Mean
# x_bar = sample
# mu = population


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
# Variance
# sigma^2 = sum((x^2)*p(x)-mu^2)
# Standard Variation
# sigma = sqrt(variance)
# Mean
# mu = sum(x*p(x))


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


def error():
    print("\nThat did not work.",)


try:
    problem = int(input("What are you solving for? "))
    if problem == 1:
        random_mean()
    elif problem == 2:
        probability_distribution()
    else:
        exit()

except statistics.StatisticsError:
    print("\nPlease enter at least 2 values.\n")
    random_mean()
    probability_distribution()

except ValueError:
    print("\nThat did not work.  Please enter a numerical value.\n")
    random_mean()
    probability_distribution()

# except TypeError:
# error()
