"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        res = []

        def dfs(node,parent,lvl):
            if not node or len(res) == 2:
                return
            else:

                if node.val == x or node.val == y:
                    res.append((parent,lvl))

                dfs(node.left,node,lvl+1)
                dfs(node.right,node,lvl+1)

        dfs(root,None,0)
        return res[0][0] != res[1][0] and res[0][1] == res[1][1]



solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
res = solution.isCousins(root, 5, 4)
print(res)
