#!/usr/bin/python

"""
    Description: Take a list such as  [8,9,10,11,12,13] or ["Alan", "Betty", "David", "Edward", "Frank", "George"]
    and return a new randomized list for each time it's run. Check to make sure the list is smaller than 1
    print out - list must contain 2 or more items
    example1: [12, 9, 11, 10, 13, 8]
    example2: ['Edward', 'George', 'Betty', 'Frank', 'David', 'Alan']
    example3: [9] prints out list must contain 2 or more items
    Developer: Rob Marchetti
"""


import random


def randomize_it(lst):
    if len(lst) <= 1:
        print("list must contain 2 or more items")
    else:
        new_lst = [w for w in random.sample(lst, len(lst))]
        return list(new_lst)


# Examples
lst1 = [8, 9, 10, 11, 12, 13]
lst2 = ["Alan", "Betty", "David", "Edward", "Frank", "George"]
lst3 = [9]

results1 = randomize_it(lst1)
results2 = randomize_it(lst2)
results3 = randomize_it(lst3)

print(results1)
print(results2)
print(results3)
