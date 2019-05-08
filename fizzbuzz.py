"""
    Description: "Write a program that prints the numbers from 1 to 100.
    But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
    For numbers which are multiples of both three and five print “FizzBuzz”."
    Developer: Rob M.
"""


def get_fizz_buzz(multiples, *args):
    for i in range(*args):
        output = ''
        for multiple in multiples:
            if i % multiple == 0:
                output += multiples[multiple]
        if output == '':
            output = i
        print(output)


# example
mults = {3: "Fizz", 5: "buzz"}
get_fizz_buzz(mults, 1, 101)



