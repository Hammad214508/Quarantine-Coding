"""
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
      palindrome = ""
      size = len(s)
      for x in range(size):
         for y in range(x, size):
             string  = s[x:y+1]
             if string == string[::-1]:
                 if len(string) > len(palindrome):
                     palindrome = string
      return palindrome
