"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
class Solution:
    def findMin(self, nums):
        def bin_dfs(start, end):
            if end - start <=  1:
                self.Min = min(nums[start], nums[end], self.Min)
                return

            mid = (start + end)//2
            if nums[end] <= nums[mid]:
                bin_dfs(mid + 1, end)
            if nums[end] >= nums[mid]:
                bin_dfs(start, mid)

        self.Min = float("inf")
        bin_dfs(0, len(nums) - 1)
        return self.Min

    
