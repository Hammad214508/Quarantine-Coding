"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        low = 0
        high = len(nums)-1
        pos = 0
        while low <= high:
            mid = low+ (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
                pos = mid+1
            else:
                high = mid-1
                pod = mid
        return pos

solution = Solution()
nums = [1,3,5,6]
target = 2
res = solution.searchInsert(nums, target)
print(res)
