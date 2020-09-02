"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3, t = 0
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1, t = 2
    Output: true

Example 3:
    Input: nums = [1,5,9,1,5,9], k = 2, t = 3
    Output: false
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        # regular duplication
        if t == 0 and len(set(nums)) == len(nums):
            return False

        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

solution = Solution()
nums = [1,2,3,1]
k = 3
t = 0
res = solution.containsNearbyAlmostDuplicate(nums, k, t)
print(res)
