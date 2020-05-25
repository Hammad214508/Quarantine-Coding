"""
Maximum Sum Circular SubarrayGiven a circular array C of integers represented by A,
find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.
(Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j
with k1 % A.length = k2 % A.length.)

Example 1:
    Input: [1,-2,3,-2]
    Output: 3
    Explanation: Subarray [3] has maximum sum 3

Example 2:
    Input: [5,-3,5]
    Output: 10
    Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
    Input: [3,-1,2,-1]
    Output: 4
    Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
    Input: [3,-2,2,-3]
    Output: 3
    Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
    Input: [-2,-3,-1]
    Output: -1
    Explanation: Subarray [-1] has maximum sum -1


Note:
    -30000 <= A[i] <= 30000
    1 <= A.length <= 30000
"""

class Solution:
    def maxSubArray(self, A):
        maxSum = A[0]
        curSum = A[0]
        for i in range(1, len(A)):
            curSum = max(A[i], curSum+A[i])
            maxSum = max(maxSum, curSum)
        return maxSum

    def maxSubarraySumCircular0(self, A: [int]) -> int:
        size = len(A)
        maxSum = self.maxSubArray(A)
        for i in range(size):
            A.append(A[0])
            del A[0]
            maxSum = max(maxSum, self.maxSubArray(A))
        return maxSum

    def maxSubarraySumCircular(self, A: [int]) -> int:
        k = self.maxSubArray(A)
        cs  = 0
        for i in range(len(A)):
            cs += A[i]
            A[i] = -A[i]
        cs += self.maxSubArray(A)
        if cs > k and cs != 0:
            return cs
        return k


solution = Solution()
list1 = [1,-2,3,-2]
list2 = [5,-3,5]
list3 = [3,-1,2,-1]
list4 = [3,-2,2,-3]
list5 = [-2,-3,-1]
res = solution.maxSubarraySumCircular(list3)
print(res)
