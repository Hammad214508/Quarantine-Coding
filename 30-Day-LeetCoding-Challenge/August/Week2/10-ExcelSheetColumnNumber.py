"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""

class Solution:
    def titleToNumber(self, s: str) -> int:

		#dict to hold letter and its serial number
        LETTERS = {letter: index for index, letter in enumerate(ascii_uppercase, start=1)}

        col_num = 0

		#convert the like 26-base number to decimal
        for i in range(len(s)):
            col_num += LETTERS[s[-1 - i]] * (26 ** i)

        return col_num
