"""
Given a binary tree where each path going from the root to any leaf form a valid sequence,
check if a given string is a valid sequence in such binary tree.

We get the given string from the concatenation of an array of integers arr and the
concatenation of all values of the nodes along a path results in a sequence
in the given binary tree.



Example 1:
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation:
    The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
    Other valid sequences are:
    0 -> 1 -> 1 -> 0
    0 -> 0 -> 0

Example 2:
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false
Explanation:
    The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.

Example 3:
Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation:
    The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isLeaf(self, node):
        return (node.left == None and node.right == None)

    def dfs(self, root, arr, index, n):
        if not root:
            return n == 0

        if self.isLeaf(root) and root.val == arr[index] and (index == n - 1):
            return True

        if index < n-1 and root.val == arr[index]:
            return self.dfs(root.left, arr, index+1, n) or self.dfs(root.right, arr, index+1, n)

        return False

    def isValidSequence(self, root: TreeNode, arr: [int]) -> bool:
        return self.dfs(root, arr, 0, len(arr))




solution = Solution()
arr = [0,1,0,1]
root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.left.right.right = TreeNode(0)
root.left.left.left = TreeNode(1)
root.right = TreeNode(0)
root.right.right = TreeNode(0)
print(solution.isValidSequence(root, arr))
