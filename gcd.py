"""
Rob Marchetti
Description: Given two numbers find greatest common denominator
"""


def gcd(a, b):
    """find greatest common denominator."""
    while b != 0:
        t = a
        a = b
        b = t % b
    return a


# example gcd is 5
# print(gcd(125, 5))





