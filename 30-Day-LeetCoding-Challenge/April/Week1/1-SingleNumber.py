"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

# This solution takes  O(n) however also uses extra memory in the hashmap O(n)
def singleNumber(nums: [int]) -> int:
    hash = {}
    for num in nums:
        hash[num] = hash.get(num, 0) + 1
    for number, count in hash.items():
        if count == 1:
            return number



# The best solution is to use XOR. XOR of all array elements gives us the number
#  with single occurrence. The idea is based on following two facts.
# a) XOR of a number with itself is 0.
# b) XOR of a number with 0 is number itself.

# [7, 3, 5, 4, 5, 3, 4]
# Let ^ be xor operator.
# res = 7 ^ 3 ^ 5 ^ 4 ^ 5 ^ 3 ^ 4
# Since XOR is associative and commutative, above
# expression can be written as:
#
# res = 7 ^ (3 ^ 3) ^ (4 ^ 4) ^ (5 ^ 5)
#     = 7 ^ 0 ^ 0 ^ 0
#     = 7 ^ 0
#     = 7
def singleNumber(nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = ans ^ nums[i]
    return ans
