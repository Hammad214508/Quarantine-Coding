"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not
flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
# n this problem we need to understand, what exactly surrouned by 'X' means.
# It actually means that if we start from 'O' at the border, and we traverse only 'O',
#  only those 'O' are not surrouned by 'X'. So the plan is the following:
#
# Start dfs or bfs from all 'O', which are on the border.
# When we traverse them, let us color them as 'T', temporary color.
# Now, when we traverse all we wanted, all colors which are not 'T' need to renamed to 'X'
# and all colors which are 'T' need to be renamed to 'O'.
class Solution:

    def dfs(self, i, j):
          if i<0 or j<0 or i>=self.M or j>=self.N or self.board[i][j] != "O":
              return
          self.board[i][j] = 'T'
          neib_list = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]
          for x, y in neib_list:
            self.dfs(x, y)

    def solve(self, board):
        if not board:
            return 0

        self.board =  board
        self.M = len(board)
        self.N = len(board[0])

        for i in range(0, self.M):
            self.dfs(i,0)
            self.dfs(i,self.N-1)

        for j in range(0, self.N):
            self.dfs(0,j)
            self.dfs(self.M-1,j)

        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] != "T":
                    board[i][j] = "X"
                else:
                    board[i][j] = "O"
        return board


solution = Solution()

board =[["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]

res = solution.solve(board)
for row in res:
    print(row)
