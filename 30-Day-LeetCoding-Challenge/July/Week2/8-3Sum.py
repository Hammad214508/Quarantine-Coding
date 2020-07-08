"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

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
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
                if sum == 0:
                    sum_zero.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                elif sum < 0:
                    start +=1
                else:
                    end -= 1
        return sum_zero
