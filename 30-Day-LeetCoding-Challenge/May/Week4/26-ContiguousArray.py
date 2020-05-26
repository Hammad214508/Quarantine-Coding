"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

class Solution:
    def findMaxLength(self, nums:[int]) -> int:
        first_p = dict()
        last_p = dict()
        first_p[0] = 0
        running_sums = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                running_sums += 1
            else:
                running_sums -= 1
            if running_sums in first_p:
                last_p[running_sums] = i+1
            else:
                first_p[running_sums] = i+1
        fans = 0

        for i in last_p:
            fans = max(fans, last_p[i] - first_p[i])
        return fans

solution = Solution()
a = [0,0,1,1,1,0,0,0,0,1,1,1]
res = solution.findMaxLength(a)
print(res)
