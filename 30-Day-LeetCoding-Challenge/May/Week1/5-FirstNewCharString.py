"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


solution = Solution()
s = "loveleetcode",
sol = solution.firstUniqChar(s)
print(sol)
