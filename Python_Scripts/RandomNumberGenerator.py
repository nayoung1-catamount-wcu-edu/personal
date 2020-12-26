# This code is an attempt to use a random number generator to eventually
# create a 5 number summary.

# User input for the lowest value in a range.
import random
import sys
import plotly.express as px

sys.tracebacklimit = 0


def random_num_gen(range_low, range_high, vars):
    """
    inputs:
        range_low : int : starting value for range
        range_high : int : ending value for range
        vars : int : number of values of produce
    outputs:
        list : vars number of random values in the specified range
    """
    if vars > range_high:
        raise ValueError("This program does not repeat values.  The number of values is greater than max range.")

    # Using the stated range to find 15 random variables and add it to a list.
    random_list = random.sample(range(range_low, range_high), vars)

    return random_list