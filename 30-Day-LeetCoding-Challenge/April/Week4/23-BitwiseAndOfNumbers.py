"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise
AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""
import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # If you starting a 0 then the answer will also be 0
        if m == 0:
            return 0
        # If m and n are on different sides of nearest power of 2
        # then the result will be zero.
        top = int(math.log(n,2))
        bottom = int(math.log(m,2))
        if top != bottom:
            return 0
        # Calculate the bitwise and between the range 
        res = m
        for num in range(m+1, n+1):
            res &= num
        return res

solution = Solution()
m = 5
n = 7
solution.rangeBitwiseAnd(m, n)
