import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ValueError
    return b / a
def log(a, b):
    if b <= 0:
        raise ValueError
    return math.log(b, a)
def exp(a, b):
    a ** b

def add(a, b): 
    return a + b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        return ValueError
    return b/a
def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(a) / math.log(b)
def exponent(a, b):
    return a ** b
