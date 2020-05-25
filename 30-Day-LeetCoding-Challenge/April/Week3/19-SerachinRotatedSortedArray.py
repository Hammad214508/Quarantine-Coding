"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

class Solution:
    # Normal binary seach
    def binarySearch(self, arr, start, end, x):
        l = start
        r = end
        while l <= r:
            mid = l + (r - l)//2;
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    # Finds the smallest element so that the lists on both sides are sorted
    def findSmallestElement(self, arr, low, high):
        if (high < low):
            return -1
        if (high == low):
            return low
        mid = int((low + high)/2)
        if (mid < high and arr[mid] > arr[mid+1]):
            return (mid+1)
        if (mid > low and arr[mid] < arr[mid - 1]):
            return mid-1
        if (arr[low] >= arr[mid]):
            return self.findSmallestElement(arr, low, mid-1);
        return self.findSmallestElement(arr, mid+1, high)

    # Find the pivot so that he lists of both sides are sorted
    # Checck which side the target is in
    # binary search that array
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        pivot = self.findSmallestElement(nums, 0, len(nums)-1)
        start = 0
        end = len(nums)
        if pivot == -1:
            return self.binarySearch(nums, start, end-1, pivot)
        if nums[pivot] == target:
            return pivot
        if nums[start] <= target:
            ans = self.binarySearch(nums, start, pivot-1, target)
        else:
            ans = self.binarySearch(nums, pivot+1, end-1, target)
        return ans

nums = [4,5,6,7,0,1,2]
target = 0
solution = Solution()
print(solution.search(nums, target))
