"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

def letterCombinations(digits):
    mapping = {
           "0": [],
           "1": [],
           "2": ["a", "b", "c"],
           "3": ["d", "e", "f"],
           "4": ["g", "h", "i"],
           "5": ["j", "k", "l"],
           "6": ["m", "n", "o"],
           "7": ["p", "q", "r", "s"],
           "8": ["t", "u", "v"],
           "9": ["w", "x", "y", "z"]
            }

    if len(digits) == 0:
        return []

    ans = mapping[digits[-1]]

    if len(digits) == 1:
        return ans

    for i in range(len(digits)-2,-1,-1):
        digit = digits[i]
        temp = []
        for c in mapping[digit]:
            temp += [c+x for x in ans]
        ans = temp
    return ans

print(letterCombinations("23"))
