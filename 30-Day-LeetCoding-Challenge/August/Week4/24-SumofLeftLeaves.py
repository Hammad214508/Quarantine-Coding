"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, side):
        if not root: return

        if not root.left and not root.right:
            if side == -1: self.sum += root.val

        self.dfs(root.left, -1)
        self.dfs(root.right, 1)

    def sumOfLeftLeaves(self, root):
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
