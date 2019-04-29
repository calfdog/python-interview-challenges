"""
    Description: A Fizz buzz example, that allow easy control to change multiples and range
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
get_fizz_buzz(mults, 1, 999)



