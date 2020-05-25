"""
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

# O(n)
def maxSubArray(nums:[int]) -> int:
    maxSum = nums[0]
    curSum = nums[0]
    for i in range(1, len(nums)):
        # Current max is either the current element or the previous sum+current element
        curSum = max(nums[i], curSum+nums[i])
        # Maximum sum so far is the current sum or the previous sum
        maxSum = max(maxSum, curSum)
    return maxSum
