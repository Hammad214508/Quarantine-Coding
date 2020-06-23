"""
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last,
    is completely filled, and all nodes in the last level are as far left as possible.
    It can have between 1 and 2h nodes inclusive at the last level h.

Example:
    Input:
        1
       / \
      2   3
     / \  /
    4  5 6

    Output: 6
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0;

        l_nodes = self.countNodes(root.left)
        r_nodes = self.countNodes(root.right)
        return l_nodes + r_nodes + 1

solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
res = solution.countNodes(root)
print(res)
