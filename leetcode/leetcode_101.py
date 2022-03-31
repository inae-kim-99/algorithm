# https://leetcode.com/problems/symmetric-tree/
# leetcode 101 : Symmetric Tree
# LEVEL : Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_q = [root.left]
        right_q = [root.right]
        
        while left_q and right_q:
            left_node = left_q.pop(0)
            right_node = right_q.pop(0)
            
            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False
            
            left_q.append(left_node.left)
            left_q.append(left_node.right)
            right_q.append(right_node.right)
            right_q.append(right_node.left)
        
        return True
                