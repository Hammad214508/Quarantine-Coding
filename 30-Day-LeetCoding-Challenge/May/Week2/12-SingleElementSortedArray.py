"""
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""
class Solution:
    # O(n) with O(n) memory
    def singleNonDuplicate0(self, nums: [int]) -> int:
        counts = dict()
        for i in nums:
          counts[i] = counts.get(i, 0) + 1
        for k, v in counts.items():
            if v == 1:
                return k

    # O(log n) with O(1) memory
    def singleNonDuplicate(self, nums: [int]) -> int:
        left =  0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # If the index is odd and the previous value is the same that means it's fine so far
            # so must be in the second half
            if mid % 2 == 1 and nums[mid - 1] == nums[mid]:
                left = mid + 1
            # If it's a even position and the next element is not the same then it's also fine
            # so far so it must be in the second half
            elif  mid % 2 == 0 and nums[mid + 1] == nums[mid]:
                left = mid + 2
            # Otherwise it is in the left half
            else:
                right = mid
        return nums[left]


solution = Solution()
input1 = [1,1,2,3,3,4,4,8,8]
input2 = [3,3,7,7,10,11,11]
res = solution.singleNonDuplicate(input1)
print(res)
