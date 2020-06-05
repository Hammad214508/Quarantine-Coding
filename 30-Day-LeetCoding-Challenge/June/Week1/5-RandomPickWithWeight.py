"""
Given an array w of positive integers, where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:
    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.

Example 1:
Input:
    ["Solution","pickIndex"]
    [[[1]],[]]
Output: [null,0]

Example 2:
Input:
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument,
the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
import random

# TIME LIMIT EXCEEDED
# class Solution:
#
#     def __init__(self, w: [int]):
#         self.weight = w
#         n = len(self.weight)
#         self.newList = []
#         for i in range(n):
#             self.newList  += self.weight[i]*[i]
#         self.length = len(self.newList)
#
#     def pickIndex(self) -> int:
#         ran = random.randint(0, self.length-1)
#         return self.newList[ran]

class Solution:

    def __init__(self, w: [int]):
        total = 0
        self.sums = []
        for weight in w:
            total += weight
            self.sums.append(total)

    def pickIndex(self) -> int:
        ran = self.sums[-1] * random.random()
        low = 0
        high = len(self.sums)
        while low<high:
            mid = low+(high-low)//2
            if ran > self.sums[mid]:
                low = mid+1
            else:
                high = mid
        return low

w = [3, 1]
solution = Solution(w)
param_1 = solution.pickIndex()
print(param_1)
