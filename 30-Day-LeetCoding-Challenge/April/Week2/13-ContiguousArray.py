"""
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation:
    [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation:
    [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

# O(n^2)
# Time limit exceeded
# The brute force approach is really simple.
# We consider every possible subarray within the given array and
# count the number of zeros and ones in each subarray.
# Then, we find out the maximum size subarray with equal no.
# of zeros and ones out of them.
def findMaxLength0(nums:[int]) -> int:
    maxLength = 0
    for x in range(len(nums)):
        numZeros = 0
        numOnes = 0
        size = 0
        for y in range(x, len(nums)):
            size += 1
            if nums[y] == 0:
                numZeros += 1
            elif nums[y] == 1:
                numOnes +=1
            if numZeros == numOnes:
                maxLength = max(maxLength, size)
    return maxLength


# The idea is that if you get a 1 increment, if 0 decrement and If the same sum
# is encountered again that means the elemens in between have a net sum of 0 meaning
# there are equal number of zeros and ones
# At the end the final answer is the largest difference between first and last instance
# a sum appeared
def findMaxLength(nums:[int]) -> int:
    first_p = dict() # first_p is the first time a sum is reached
    last_p = dict() # last_p if the last time a sum has been reached
    first_p[0] = 0
    # This is incremented if there's a 1 and decremented if there is a 0.
    running_sums = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            running_sums += 1
        else:
            running_sums -= 1
        if running_sums in first_p:
            last_p[running_sums] = i+1
        else:
            first_p[running_sums] = i+1
    fans = 0
    for i in last_p:
        fans = max(fans, last_p[i] - first_p[i])
    return fans
