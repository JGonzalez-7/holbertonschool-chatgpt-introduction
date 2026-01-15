#!/usr/bin/python3
import sys

# Function description:
#   Compute the factorial of a non-negative integer using recursion.
# Parameters:
#   n (int): Non-negative integer whose factorial will be computed.
# Returns:
#   int: Factorial of n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
