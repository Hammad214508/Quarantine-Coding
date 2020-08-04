"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num & (num - 1)  and len(bin(num)) % 2 
