"""
    Simple example to find all the palindromes for a range of numbers
    Developer: Rob Marchetti
"""

def is_palindrome(*args):
    for i in range(*args):
        num = str(i)
        if num == num[::-1]:
            print("This is a palindrome {}", num)
        else:
            print("This is not a palindrome {}".format(num))

# Example
is_palindrome(1, 99)