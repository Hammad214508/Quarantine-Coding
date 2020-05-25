"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all
the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any
            prefix or suffix of the array (including the whole array)
            fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

# O(n) but uses the division operator
# productExceptSelf(nums:[int]) -> [int]:
def productExceptSelf0(nums):
    product = 1
    for elem in nums:
        product *= elem
    output = []
    for elem in nums:
        output.append(product/elem)
    return output


def productExceptSelf(nums):
    length = len(nums)
    L = [0]*length
    R = [0]*length
    output = [0]*length
    L[0] = 1
    for i in range(1, length):
        L[i] = nums[i-1]*L[i-1]
    R[len(nums) - 1] = 1
    for i in range(length - 2, -1, -1):
        print(i)
        R[i] = nums[i + 1] * R[i + 1]
    for i in range(length):
        output[i] = L[i] * R[i]
    return output

print(productExceptSelf([1,2,3,4]))
