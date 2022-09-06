# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# leetcode 129 : Sum Root to Leaf Numbers
# LEVEL : Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []

        def sumNumber(node, before):
            if not node.left and not node.right:
                ans.append(before * 10 + node.val)
                return

            if node.left:
                sumNumber(node.left, before * 10 + node.val)
            if node.right:
                sumNumber(node.right, before * 10 + node.val)

        sumNumber(root, 0)

        return sum(ans)
