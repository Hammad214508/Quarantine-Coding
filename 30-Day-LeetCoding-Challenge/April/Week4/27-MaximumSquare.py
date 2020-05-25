"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing
only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution:
    # The simplest approach consists of trying to find out every possible
    # square of 1’s that can be formed from within the matrix.
    def maximalSquare0(self, matrix: [[str]]) -> int:
        rows = len(matrix)
        if rows>0:
            cols = len(matrix[0])
        else:
            cols = 0
        maxSquare = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    squareLen = 1
                    flag = True
                    while squareLen+i < rows and squareLen+j < cols and flag:
                        for k in range(j, squareLen+j+1):
                            if matrix[i+squareLen][k] == '0':
                                flag = False
                                break
                        for k in range(i, squareLen+i+1):
                            if matrix[k][j+squareLen] == '0':
                                flag = False
                                break
                        if flag:
                            squareLen += 1
                    maxSquare = max(maxSquare, squareLen)
        return maxSquare*maxSquare

    def maximalSquare(self, matrix: [[str]]) -> int:
        rows = len(matrix)
        if rows>0:
            cols = len(matrix[0])
        else:
            cols = 0
        dp = [[0]*(cols+1) for i in range(rows+1)]
        maxSquare = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    # Minimum of all three
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
                    maxSquare = max(maxSquare, dp[i][j])
        return maxSquare*maxSquare





matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

solution = Solution()
print(solution.maximalSquare(matrix))
