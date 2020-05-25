"""
Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ;
otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash = {}
        for letter in magazine:
            if letter in hash:
                hash[letter[0]] += 1
            else:
                hash[letter[0]] = 1
        for letter in ransomNote:
            if letter not in hash:
                return False
            elif hash[letter] == 0:
                return False
            else:
                hash[letter] -= 1
        return True

solution = Solution()
a = solution.canConstruct("aa", "ab")
print(a)
