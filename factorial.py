import math
def factorial(n):
    if n < 0:
        return "factorial is not for negative num"
    else:
        return math.factorial(n)

print(factorial(10))


def factorial(y):
    if y < 0:
        return "undefined"
    else:
        if y == 0 and y == 1:
            return 1
        else:
            return y*factorial(y-1)

print(factorial(6))