"""
    Description: A Fizz buzz example, that allow easy control to change multiples and range
    Developer: Rob M.
"""

def get_fizzbuzz(multiples, *args):
    for i in range(*args):
        output =''
        for multiple in multiples:
            if i % multiple == 0:
                output += multiples[multiple]
        if output == '':
            output = i
        print(output)



# example
multiples = {3:"Fizz", 5:"buzz"}
get_fizzbuzz(multiples, 1, 999)



