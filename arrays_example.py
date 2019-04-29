"""
    Given an array of integers, return indices
    of the two numbers such that they add up to a specific target.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

def find_nums(nums, target):

    for x in nums:
        for y in nums:
            if x + y == target:
                return (nums.index(x), nums.index(y))

# Example
arr = [2, 7, 11, 15]
target = 9
result = find_nums(arr, target)
print(result)