"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of node.right
has a value > node.val.  Also recall that a preorder traversal displays the value
of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Output: [8,5,10,1,7,null,12]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def addBinaryTree(self, root, value):
        if not root:
            return TreeNode(value)
        if value < root.val:
            root.left = self.addBinaryTree(root.left, value)
        else:
            root.right = self.addBinaryTree(root.right, value)
        return root

    def print_tree(self, root):
        if root:
            print(root.val)
            self.print_tree(root.left)
            self.print_tree(root.right)


    def bstFromPreorder(self, preorder: [int]) -> TreeNode:
        root = None
        for elem in preorder:
            root = self.addBinaryTree(root, elem)
        self.print_tree(root)
        return root


input = [8,5,1,7,10,12]
solution = Solution()
solution.bstFromPreorder(input)
