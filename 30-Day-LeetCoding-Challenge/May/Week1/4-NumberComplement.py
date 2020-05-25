"""
Given a positive integer, output its complement number.
The complement strategy is to flip the bits of its binary representation.

Example 1:
Input: 5
Output: 2
Explanation:
    he binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
    So you need to output 2.


Example 2:
Input: 1
Output: 0
Explanation:
    The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

# Returns the string version of the binary representation of a number
# It is reversed
def findBinary(num):
    bin = ""
    while num > 0:
        bin += str(num%2)
        num = num//2
    return bin

# Given a binary string (reversed) find the integer value equivalent to it
def findInt(binary):
    intVal = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            intVal += 2**i
    return intVal

class Solution:
    def findComplement(self, num: int) -> int:
        # Get the binary representation
        bin = findBinary(num)
        binComplement = ""
        # Complement the representation
        for digit in bin:
            if digit == "0":
                binComplement += "1"
            else:
                binComplement += "0"
        # Find the integer representation of the complement
        intVal = findInt(binComplement)
        return intVal


solution = Solution()
a = solution.findComplement(1)
print(a)
