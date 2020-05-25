"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
# Change the problem a little so instead of going from (0, 0) to (m, n) it's
# from (m, n) to (0, 0) moving only UP or LEFT. This is only so that I don't have
# to have reverse loops
# Each position in he grid will hold the minimum distance to get to that point
class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # Fill the first row as the sum as you can only go left
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        # Fill the first colum as the sum as you can only go up
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        # For the other cells choose the minimum of the two options available
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        # Return the value in the top botom cell
        return grid[m-1][n-1]


grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]

solution = Solution()
print(solution.minPathSum(grid))
