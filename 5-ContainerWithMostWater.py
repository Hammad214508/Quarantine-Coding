"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
# Too slow for large lists
def maxArea0(height):
    finalArea = 0
    for x in range(len(height)):
        currMax = 0
        for y in range(len(height)):
            h = min(height[x], height[y])
            w = y-x
            area = h*w
            currMax = max(currMax, area)
        finalArea = max(finalArea, currMax)
    return finalArea

def maxArea(height):
    left_pointer = 0
    right_pointer = len(height)-1
    maxArea = 0
    while left_pointer < right_pointer:
        h = min(height[left_pointer], height[right_pointer])
        w = right_pointer - left_pointer
        area = h * w
        maxArea = max(maxArea, area)
        if height[left_pointer] < height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1
    return maxArea
