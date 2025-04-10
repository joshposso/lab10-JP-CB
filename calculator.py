# https://github.com/joshposso/lab10-JP-CB
# Partner 1: Josh Posso
# Partner 2: Callahan Bonifant
import math

def add(a, b):
    return a + b

def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def exp(a, b):
  return a ** b

def subtract(a,b):
    return a-b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math.hypot(a, b)


def logarithm(a, b):
    if a <= 0:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(a,b)
