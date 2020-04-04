"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c
in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

# Brute Force Approach
# Still includes repeated values
# O(n^3)
def threeSum0(nums):
    sum_zero = []
    n = len(nums)
    for x in range(0, n-2):
        for y in range(x+1, n-1):
            for z in range(y+1, n):
                if (nums[x]+nums[y]+nums[z]) == 0:
                    sum_zero.append([nums[x], nums[y], nums[z]])

    return sum_zero

# Runtime: O(n^2)
# Space: O(n)
def threeSum(nums):
    nums.sort() # Sort the array
    n = len(nums)
    sum_zero = []
    # Have three indexes
    for i in range(n-1):
        start = i + 1
        end = n - 1
        # To ignore duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while (start < end):
            # To ignore duplicates
            if end < n - 1 and nums[end] == nums[end + 1]:
                end -=1
                continue
            sum = nums[i] + nums[start] + nums[end]
            # Change the pointers according the the sum value and store if 0
            if sum == 0:
                sum_zero.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
            elif sum < 0:
                start +=1
            else:
                end -= 1
    return sum_zero
