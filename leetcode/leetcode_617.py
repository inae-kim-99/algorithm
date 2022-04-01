# https://leetcode.com/problems/merge-two-binary-trees/
# leetcode 617 : Merge Two Binary Trees
# LEVEL : Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        elif root1 and not root2:
            return root1
        elif not root1 and root2:
            return root2
        
        tree = [(root1, root2)]
        
        while tree:
            node1, node2 = tree.pop(0)
                
            node1.val += node2.val
            
            if node2.left:
                if node1.left:
                    tree.append((node1.left, node2.left))
                else:
                    node1.left = node2.left
            if node2.right:
                if node1.right:
                    tree.append((node1.right, node2.right))
                else:
                    node1.right = node2.right
        
        return root1
                
            
        
        