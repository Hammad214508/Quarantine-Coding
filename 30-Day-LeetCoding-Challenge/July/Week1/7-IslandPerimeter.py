"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
 and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""

class Solution:
    def islandPerimeter(self, grid: [[int]]) -> int:
        m, n, Perimeter = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                Perimeter += 4*grid[i][j]
                if i > 0:   Perimeter -= grid[i][j]*grid[i-1][j]
                if i < m-1: Perimeter -= grid[i][j]*grid[i+1][j]
                if j > 0:   Perimeter -= grid[i][j]*grid[i][j-1]
                if j < n-1: Perimeter -= grid[i][j]*grid[i][j+1]
        return Perimeter
    
solution = Solution()
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

res = solution.islandPerimeter(grid)
print(res)
