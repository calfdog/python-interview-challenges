"""
    Given an array of integers, return indices
    of the two numbers such that they add up to a specific target.

    Example:
    Given nums = [7, 5, 11, 4], target = 9,
    Because nums[1] + nums[3] = 5 + 4 = 9,
    return [1, 3].
"""


def find_nums(nums, target):
    for x in nums:
        for y in nums:
            if x + y == target:
                return nums.index(x), nums.index(y)


# Simple example
arr = [7, 5, 11, 4]
target_num = 9
result = find_nums(arr, target_num)
print(result)

