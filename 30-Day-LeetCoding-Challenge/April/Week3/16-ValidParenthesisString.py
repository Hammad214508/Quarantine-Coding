"""
Given a string containing only three types of characters: '(', ')'
and '*', write a function to check whether this string is valid.
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis
'(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
"""

# checkValidString(s: str) -> bool:
def checkValidString(s):
    low = 0
    high = 0
    for c in s:
        if c =='(':
            low += 1
        else:
             low -= 1
        if c != ')':
            high += 1
        else:
            high -= 1
        if high < 0:
            break
        low = max(low, 0)
    return low == 0


        if s=="":
            return True
            
def checkValidString(s):
        n = len(s)
        left,right = 0,0 # keep count of left and right brackets
        for i in range(0,n):
            x = s[i] # left side
            y = s[n-i-1] # right side
            if x =="*" or x=="(":
                left+=1
            else:
                left-=1

            if y=="*" or y==")":
                right+=1
            else:
                right-=1

            if right<0 or left<0:
                return False

        return True
