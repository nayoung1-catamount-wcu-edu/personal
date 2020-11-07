# Math_475 Week 2 Class Notes

## Overview of Machine Learning

Questions ML can possibly answer:

- Will this user buy the upgrade pack for our game?
- How many emergency room patients will arrive overnight tonight?
- Is this purchase being made with a stolen credit card?
- Will this college basketball player play at least one regular season game in the NBA?
- Should this person be recommended for a cancer diagnostic?

  - No such thing as a free lunch

- for a certain type of mathematical problems, the computational cost of finding a solution, averaged over all problems in the class, is the same for any solution method. No solution therefore offers a "short cut"

## What is Machine Learning

"The field of study that allows computers to learn without being explicitly programmed."

- commonly attributed to Arthur Samuel, 1959?

"A computer can be programmed so that it will learn to play a better game of checkers than can be played by the person who wrote the program."

## Types of problems we will encounter

Two types of variables

- Features

  - predictors, inputs, independent variables

- Target

  - response, output, depended variables

- Observation

  - a single element of a data set

## Regression

A _regression_ problem is one where we predict a _continuous numerical target variable_, based on its features.

## Classification

A _classification_ problem is one where we predict which _class_ an observation will belong to, based on its features.

--------------------------------------------------------------------------------

In a typical situation where you will deal with regression...

- most of the work comes before you do the code to build the model

  - look at your data
  - which features are important?

    - what types of relationships do the features appear to have with the target?

## Simple Linear Regression

- One feature
- One target

f(x) = w*x + b

- b = bias

f(x) = w1x + w0

- w = weights
- most likely in machine learning

--------------------------------------------------------------------------------

## Math_475 Video Notes

## Python functions, Part 1

To find f(x) = x^2

```python
def square(x):
    y = x * x
    return y
```

Once we have defined a function, we can evaluate it by plugging in an appropriate argument.

```python
my_num = square(3)
print(my_num)
```

You may think of a function according to your algebra/calculus intuition, with something like:

g(x) = 3 * x^2 - 1

Notice what this definition contains:

- g: the function name
- x: the input to the function
- an algorithm for computing the output:

  1. square x
  2. multiply the result from step 1 by 3
  3. subtract 1 from the result in step 2
  4. the result from step 3 is your final answer

```python
def g(x):
    step1 = x*x
    step2 = 3*step1
    step3 = step2 - 1
    return step3
```

This is not the only way to do this:

```python
def alt_g(x):
    return 3*x**2 - 1
```

We can also have functions in python that take more than one argument:

```python
def add_two_numbers(num1, num2):
    return num1 + num2

def x_minus_y_to_the_n(x,y,n):
    return (x-y)**n
```

--------------------------------------------------------------------------------

## Mathematical Functions

Mathematically speaking, two functions are **the same** (equal) if they have:

- the same domain
- the same codomain
- the same outputs over all inputs

--------------------------------------------------------------------------------

## Item 7 -- Overview of the Linear Modeling Process

The Process

1. Decide to use a linear model
2. Decide which features to use
3. Decide how to avoid overfitting
4. Train the model
5. Check the model

Decide Which Features to Use

- There are two types of changes that we can make to our data to potentially improve our model.

  - get rid of features that have issues

    - Feature selection

  - add new features to account for nonlinear relationships

    - feature engineering

## Item 13a: The Correlation Coefficient Explained in 1 min

[video](https://www.youtube.com/watch?v=WpZi02ulCvQ)

## Item 13b: The Visual Intuition Behind the Correlation Coefficient

[video](https://www.youtube.com/watch?v=ugd4k3dC_8Y)

## Item 15: Regression Practice Activity #1 -- Cricket Data

[notebook](Week2_Item15.ipynb)
