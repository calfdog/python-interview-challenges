"""
    Simple example to find all the palindromes for a range of numbers
    Developer: Rob Marchetti
"""

def is_number_palindrome(*args):
    for i in range(*args):
        # ignore integers under 10
        if i >= 10:  # set to another number to change the start
            # change int to string
            num = str(i)
            # if the num matches the num reversed if a palindrome
            if num == num[::-1]:
                print("{} is a palindrome".format(num))
            else:
                print("{} is not a palindrome".format(num))


# Example - enter start,end (1,99) or just (99)
is_number_palindrome(1, 99)
