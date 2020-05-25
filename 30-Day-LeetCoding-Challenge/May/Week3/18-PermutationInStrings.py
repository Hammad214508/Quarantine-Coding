"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's2 permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation:
    s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        N = len(s1)-1
        cnt = collections.Counter(s2[:N])
        cntp = collections.Counter(s1)
        for i,c in enumerate(s2[N:]):
            cnt[c]+=1
            if cnt == cntp:
                return True
            cnt -= collections.Counter(s2[i])
        return False

solution = Solution()
s1 = "ab"
s2 = "eidbaooo"
res = solution.checkInclusion(s1, s2)
print(res)
