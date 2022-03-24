# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# leetcode 114 : Flatten Binary Tree to Linked List
# LEVEL : Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        parent = root
        while parent != None:
            if parent.left != None:
                temp = parent.right
                parent.right = parent.left
                parent.left = None

                right_leaf = parent.right
                while right_leaf.right != None:
                    right_leaf = right_leaf.right
                right_leaf.right = temp

            parent = parent.right

        return root
