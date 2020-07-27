"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
    def buildTree(self, inorder, postorder):
        def helper(post_beg, post_end, in_beg, in_end):
            if post_end - post_beg <= 0: return None
            ind = dic[postorder[post_end-1]]

            root = TreeNode(inorder[ind])
            root.left  = helper(post_beg, post_beg + ind - in_beg, in_beg, ind)
            root.right = helper(post_end - in_end + ind, post_end - 1, ind + 1, in_end)
            return root

        dic = {elem: it for it, elem in enumerate(inorder)}
        return helper(0, len(postorder), 0, len(inorder))
