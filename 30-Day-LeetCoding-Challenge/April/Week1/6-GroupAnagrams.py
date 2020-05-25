"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

def groupAnagrams(self, strs:[str]) -> [[str]]:
    groups = {} # Hashmap mapping the sorted version to the words (anagram)
    for word in strs:
        # Sort the word
        sortedWord = ""
        for letter in sorted(word):
            sortedWord += letter
        # if the sorted wor is there then store it
        if sortedWord in groups:
            groups[sortedWord].append(word)
        # Add it otherwise
        else:
            groups[sortedWord] = [word]
    return list(groups.values())
