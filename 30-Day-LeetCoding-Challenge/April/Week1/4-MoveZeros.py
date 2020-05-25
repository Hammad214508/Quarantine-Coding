"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

# O(n)
# Goes through the entire list and if it find a 0 if removes it
# and appends it at the end
def moveZeroes(nums:[int]) -> None:
    for num in nums:
        if num is 0:
            nums.remove(num)
            nums.append(num)
