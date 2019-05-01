"""
    Description: Get the List length using recursion
    Developer: Rob M.
"""


def get_list_len(lst):
    # If an empty list return zero
    if lst == []:
        return 0
    # Slice the list
    return 1 + get_list_len(lst[1:])


new_list = ["Able", "cane", 1, 2, 3, "ABC", "Ole", 0]

results = get_list_len(new_list)
print(results)
