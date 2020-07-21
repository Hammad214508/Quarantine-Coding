"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
	m, n = len(board), len(board[0])

	def search(x:int, y:int, d:int) -> bool:
		if x>=m or x<0 or y>=n or y<0 or word[d] != board[x][y]: return False
		if d == len(word)-1: return True
		temp = board[x][y]
		board[x][y] = '0' # mark visited
		found = search(x,y-1,d+1) or search(x,y+1,d+1) or search(x-1,y,d+1) or search(x+1,y,d+1)
		board[x][y] = temp
		return found

	for i in range(m):
		for j in range(n):
			if search(i, j, 0): return True
	return False

solution = Solution()
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
res = solution.exists(board)
print(res)
