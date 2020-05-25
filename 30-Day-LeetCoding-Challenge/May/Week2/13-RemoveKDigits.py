"""
Given a non-negative integer num represented as a string, remove k digits from the number
so that the new number is the smallest possible.

Note:
    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation:
    Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation:
    Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation:
    Remove all the digits from the number and it is left with nothing which is 0.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"


solution = Solution()
num = "1432219"
k = 3
res = solution.removeKdigits(num, k)
print(res)

"""
EXPLANATION:-
Suppose If we have num 1543, k = 2
Traverse through each digit in num,
if you found, previous digit is greater than the current digit, delete it.

DIGITS = 1, 5, 6, 3    K = 2  res = ""
current_digit = 1, So, res = 1
current_digit = 5, So, res = 15
current_digit = 6, So, res = 156
current_digit = 3,
		Now, previous digit (6) greater than current digit (3).
		So, del previous digit.
		res = 15  K = 1
		Still previous digit(5) is greater than current digit (3)
		res = 1, K = 0
		Now, K becomes 0
		and add remaining digits to res.
		res = 13
So, smallest number is 13.
"""
