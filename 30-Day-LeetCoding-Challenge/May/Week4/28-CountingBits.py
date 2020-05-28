"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n)
/possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
# any number's bit are duplicate of its half with additional bit.
# 10 1 (2 and 1)
# 11 1 (3 and 1)
# 100 10 (4 and 2)
# 101 10 (5 and 2)
# 110 11 (6 and 3)
class Solution:
    def countBits(self, num: int) -> [int]:
        if num == 0:
            return [num]
        out = [0,1]
        for i in range(2,num+1):
            out.append(out[i//2] + i%2)
        return out

solution = Solution()
num = 6
res = solution.countBits(num)
print(res)
