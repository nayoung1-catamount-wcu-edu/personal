#!/usr/bin/env python3.7

# This code is an attempt to create a random list of pairs and rotate them
# until all combinations have been achieved.

# Imports
import itertools

# Define variables
sets = 2

# Creates a list of sets using inputed values
for pair in itertools.combinations([1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10], sets):
    print(pair)
