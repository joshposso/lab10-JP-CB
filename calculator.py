import math
#lab 10


def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ValueError
    return b/a
def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b <= 0 or b == 1:
        raise ValueError
    return math.log(a) / math.log(b)
def exponent(a, b):
    return a ** b