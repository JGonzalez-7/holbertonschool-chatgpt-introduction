#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")  # guard against invalid input
    result = 1
    while n > 1:
        result *= n
        n -= 1  # decrement to ensure the loop terminates
    return result

f = factorial(int(sys.argv[1]))
print(f)
