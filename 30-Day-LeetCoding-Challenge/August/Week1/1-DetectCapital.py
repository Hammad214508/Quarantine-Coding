"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.


Example 1:

Input: "USA"
Output: True


Example 2:

Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)

        match1, match2, match3 = True, True, True

        # case 1: All capital
        for i in range(n):
            if not word[i].isupper():
                match1 = False
                break
        if match1:
            return True

        # case 2: All not capital
        for i in range(n):
            if word[i].isupper():
                match2 = False
                break
        if match2:
            return True

        # case 3: All not capital except first
        if not word[0].isupper():
            match3 = False
        if match3:
            for i in range(1, n):
                if word[i].isupper():
                    match3 = False
        if match3:
            return True

        # if not matching
        return False
