"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def cumSum(self, root):
        self.n += 1
        for child in filter(None, [root.left, root.right]):
            child.val += root.val
            self.cumSum(child)

    def dfs(self, root, sum):
        if not root: return None

        self.count[root.val + sum] += 1
        self.result += self.count[root.val]
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.count[root.val + sum] -= 1

    def pathSum(self, root, sum):
        if not root: return 0

        self.n, self.result, self.count = 0, 0, defaultdict(int)
        self.cumSum(root)
        self.count[sum] = 1
        self.dfs(root, sum)
        return self.result  - self.n*(sum == 0) 
