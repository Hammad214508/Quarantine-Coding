"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon.
 The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned
 in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer.
If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers)
upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's
health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.



Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal
path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	    -10	1
10  	30	-5 (P)


Note:
    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
"""
from tabulate import tabulate

class Solution:

    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        dp[m-1][n] = 1
        dp[m][n-1] = 1

        for i in range(m-1):
            dp[i][n] = float("inf")
        for j in range(n-1):
            dp[m][j] = float("inf")

        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                dp[x][y] = min(dp[x+1][y], dp[x][y+1]) - dungeon[x][y]
                dp[x][y] = max(dp[x][y], 1)
                
        return dp[0][0]

solution = Solution()
dungeon = [[-2,-3,3],
           [-5,-10,1],
           [10,30,-5]]
res = solution.calculateMinimumHP(dungeon)
print(res)
