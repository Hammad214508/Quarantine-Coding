"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        queue = [root]
        answer = [[root.val]]
        while queue:
            child = []
            for node in queue:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            if not child: #last level of tree.
                break
            queue = child #assigning this level to queue.
            answer.append([node.val for node in queue])
        return answer[::-1]

solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
res = solution.levelOrderBottom(root)
print(res)
