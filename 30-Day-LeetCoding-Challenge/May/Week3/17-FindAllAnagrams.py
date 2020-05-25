"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will
not be larger than 20,100.

The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
    [0, 6]
Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
    [0, 1, 2]
Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
    # ACCEPTED
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(p)-1
        cnt = collections.Counter(s[:N])
        cntp = collections.Counter(p)
        r = []
        for i,c in enumerate(s[N:]):
            cnt[c]+=1
            if cnt == cntp: r.append(i)
            cnt -= collections.Counter(s[i])
        return r


    def isAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        d, d2 = {}, {}
        for char in str1:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        for char in str2:
            if char not in d:
                return False
            if char not in d2:
                d2[char] = 1
            else:
                d2[char] += 1
        return d == d2

    # Time Limit Exceeded
    def findAnagrams0(self, s: str, p: str) -> [int]:
        strLen = len(s)
        wordLen = len(p)
        i = 0
        output = []
        while i <= (strLen-wordLen):
            substring = s[i:i+wordLen]
            if self.isAnagram(substring, p):
                output.append(i)
            i += 1
        return output

    # Time Limit Exceeded
    def findAnagrams1(self, s: str, p: str) -> [int]:
        p = sorted(p)
        n = len(s)
        m = len(p)
        output = []
        for i in range(n-m+1):
            substring = sorted(s[i:i+m])
            if p == substring:
                output.append(i)
        return output

solution = Solution()
s = "cbaebabacd"
p = "abc"
res = solution.findAnagrams(s, p)
print(res)
