# https://leetcode.com/problems/validate-binary-search-tree/
# leetcode 98 : Validate Binary Search Tree
# LEVEL : Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root.left, -2**31-1, root.val) and self.isValid(root.right, root.val, 2**31)

    def isValid(self, node, min, max):
        if not node:
            return True
        if min < node.val < max:
            return self.isValid(node.left, min, node.val) and self.isValid(node.right, node.val, max)
        else:
            return False
