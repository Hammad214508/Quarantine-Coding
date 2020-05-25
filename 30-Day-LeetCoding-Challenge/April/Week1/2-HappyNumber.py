"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until the
number equals 1 (where it will stay), or it loops endlessly in a cycle
which does not include 1. Those numbers for which this process ends
in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

# Keep track of which values have been used
# Stop if there was a value already used, prevents cycle
# Uses extra memory to keep track of values used
# And then linear searches to checck for cycles
def isHappy0(n: int) -> bool:
    used = []
    while n != 1:
        if n in used:
            return False
        used.append(n)
        digits = [int(x) for x in str(n)]
        sum_of_squares = 0
        for digit in digits:
            sum_of_squares += digit**2
        n = sum_of_squares
    return True

# Better approch
# The number that causes an infinite cycle is 4 so loop until
# you either get a 1 or a 4. If you got a 1 then it's a happy number
# otherwise it isn't.
# Doesn't use any extra memory and no need to search through any list
def isHappy(n: int) -> bool:
    while n != 1 and n!= 4:
        digits = [int(x) for x in str(n)]
        sum_of_squares = 0
        for digit in digits:
            sum_of_squares += digit**2
        n = sum_of_squares
    if n == 1:
        return True
    else:
        return False
