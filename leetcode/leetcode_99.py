# https://leetcode.com/problems/recover-binary-search-tree/
# leetcode 99 : Recover Binary Search Tree
# LEVEL : Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        arr = []

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            arr.append(node)
            inOrder(node.right)

        inOrder(root)

        sortedArr = sorted(arr, key=lambda x: x.val)

        for i in range(len(sortedArr)):
            if sortedArr[i].val != arr[i].val:
                sortedArr[i].val, arr[i].val = arr[i].val, sortedArr[i].val
                return
