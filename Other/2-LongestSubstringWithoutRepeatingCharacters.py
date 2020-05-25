"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation:
    The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation:
    The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation:
    The answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    visited = []
    max_length = 0

    for letter in s:
        if letter in visited:
            visited = visited[visited.index(letter)+1:]
        visited.append(letter)
        max_length = max(max_length, len(visited))

    return max_length
