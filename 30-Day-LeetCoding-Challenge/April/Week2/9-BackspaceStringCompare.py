"""
Given two strings S and T, return if they are equal when both are typed into empty
text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

# This is implemented using like a stack
# So push the element from the string into the stack
# However, if it's a # then pop from the stack
# return a string of the current stacks
def processString(string):
    newStr = []
    for letter in string:
        # Remove the last element
        if letter == "#":
            if len(newStr) > 0:
                newStr.pop()
        else:
            newStr.append(letter)
    # Get a string for the stack
    return "".join(newStr)

def backspaceCompare(S: str, T: str) -> bool:
    newS = processString(S)
    newT = processString(T)
    # Check if they are equal
    return newS == newT
