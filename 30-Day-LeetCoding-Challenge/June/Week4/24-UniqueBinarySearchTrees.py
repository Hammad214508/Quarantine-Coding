"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:

    def binomialCoeff(self, n, k):
        res = 1

        # Since C(n, k) = C(n, n-k)
        if (k > n - k):
            k = n - k

        # Calculate value of [n*(n-1)*---*(n-k+1)] /
        # [k*(k-1)*---*1]
        for i in range(k):

            res *= (n - i)
            res //= (i + 1)
        return res

    def catalan(self, n):
        # Calculate value of 2nCn
        c = self.binomialCoeff(2 * n, n)
        # return 2nCn/(n+1)
        return c // (n + 1)

    def numTrees(self, n: int) -> int:
        count = self.catalan(n)
        return count

solution = Solution()
n = 3
res = solution.numTrees(n)
print(res)
