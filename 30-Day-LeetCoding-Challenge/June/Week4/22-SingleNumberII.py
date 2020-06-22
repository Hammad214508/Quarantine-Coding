"""
Given a non-empty array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,3,2]
    Output: 3

Example 2:
    Input: [0,1,0,1,0,1,99]
    Output: 99
"""
class Solution:
    def singleNumber(self, nums: [int]) -> int:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        for number, count in hash.items():
            if count == 1:
                return number

solution = Solution()
nums = [2,2,3,2]
res = solution.singleNumber(nums)
print(res)
