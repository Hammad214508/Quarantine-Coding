"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
    Input: root1 = [2,1,4], root2 = [1,0,3]
    Output: [0,1,1,2,3,4]

Example 2:
    Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
    Output: [-10,0,0,1,2,5,7,10]

Example 3:
    Input: root1 = [], root2 = [5,1,7,0,2]
    Output: [0,1,2,5,7]

Example 4:
    Input: root1 = [0,-10,10], root2 = []
    Output: [-10,0,10]

Example 5:
    Input: root1 = [1,null,8], root2 = [8,1]
    Output: [1,1,8,8]

Constraints:
    Each tree has at most 5000 nodes.
    Each node's value is between [-10^5, 10^5].
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []
        res2 = []
        # help function to merge two sorted lists
        def merge(list1, list2):
            i, j = 0, 0
            res = []
            while i<len(list1) and j<len(list2):
                if list1[i] < list2[j]:
                    res.append(list1[i])
                    i+=1
                else:
                    res.append(list2[j])
                    j+=1
            res+= list1[i:]
            res+=list2[j:]
            return res

        # help function for inorder traverse tree
        def inorder(root, my_list):
            if not root:
                return
            inorder(root.left,my_list)
            my_list.append(root.val)
            inorder(root.right,my_list)

        inorder(root1, res1)
        inorder(root2, res2)
        ans = merge(res1, res2)
        return ans
