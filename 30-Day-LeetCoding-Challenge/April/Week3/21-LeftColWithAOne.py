"""
(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix,
this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed)
with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a
BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following
four examples. You will not have access the binary matrix directly.


Example 1:
Input: mat = [[0,0],
              [1,1]]
Output: 0


Example 2:
Input: mat = [[0,0],
              [0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],
              [0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],
              [0,0,1,1],
              [0,1,1,1]]
Output: 1
"""

"""
This is BinaryMatrix's API interface.
You should not implement it, or speculate about its implementation
"""
class BinaryMatrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def dimensions(self) -> [int]:
       n = len(self.matrix)
       m = len(self.matrix[0])
       return [n, m]

# Imagine there is a pointer p(x, y) starting from top right corner. 
# p can only move left or down. If the value at p is 0, move down.
# If the value at p is 1, move left. Try to figure out the correctness
# and time complexity of this algorithm
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        rows, columns = binaryMatrix.dimensions()
        rows -= 1
        columns -= 1
        row = 0
        col = columns
        while(row <= rows and col >= 0):
            if binaryMatrix.get(row, col) == 1:
                col -= 1
            else:
                row += 1
        if col != columns:
            return col+1
        return -1


mat = [[0,0],[0,0]]
matrix = BinaryMatrix(mat)

solution = Solution()
print(solution.leftMostColumnWithOne(matrix))
