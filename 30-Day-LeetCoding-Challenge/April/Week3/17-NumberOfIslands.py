"""
Given a 2d self.grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the self.grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""

class Solution:
    # numIslands(self, self.grid: List[List[str]]) -> int:
    def __init__(self):
        self.grid = None

    def numIslands(self, grid):
        self.grid = grid
        if not self.grid:
            return 0
        self.row = len(self.grid)
        self.column = len(self.grid[0])
        islands = 0

        for i in range(self.row):
            for j in range(self.column):
                if self.grid[i][j] == '1':
					# every time we get a new land, we walk from it
					# and turn all lands that we can reach to zero
                    islands += 1
                    self.walk_through(i, j)
        return islands

    # recursively walk and remark
    # DFS
    def walk_through(self, i, j):
        self.grid[i][j] = 0
        if i-1 >= 0 and self.grid[i-1][j] == '1':
            self.walk_through(i-1, j)
        if i+1 < self.row and self.grid[i+1][j] == '1':
            self.walk_through(i+1, j)
        if j-1 >= 0 and self.grid[i][j-1] == '1':
            self.walk_through(i, j-1)
        if j+1 < self.column and self.grid[i][j+1] == '1':
            self.walk_through(i, j+1)

grid1 = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

grid2 = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]


solution = Solution()
print(solution.numIslands(grid2))
