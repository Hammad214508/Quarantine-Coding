"""
Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    # 0 Represenst the index can't take you to the end
    # 1 Represents it can
    # if the index can take you to another index that is marked as 1 then
    # this index is also 1
    # At the end return if the start index in 1
    def canJump0(self, nums: [int]) -> bool:
        n = len(nums)
        memo  = []
        # All indexes are bad at the start
        for i in range(n):
            memo.append(0)
        # last one is good
        memo[n-1] = 1
        # For each index check all the indexes it can go upto
        for i in range(n-2, -1, -1):
            furthestJump = min(i+nums[i], n-1)
            for j in range(i+1, furthestJump+1):
                # If it can go to a good one then mark it as good
                if memo[j] == 1:
                    memo[i] = 1
                    break
        # Return if the first index is good or no
        return memo[0] == 1

    def canJump(self, nums: [int]) -> bool:
        n = len(nums)
        goal = n-1
        for i in range(n-1, -1, -1):
            if i+nums[i] >= goal:
                goal = i
        return goal == 0




solution = Solution()
a = [2,3,1,1,4]
b = [3,2,1,0,4]
print(solution.canJump(a))
