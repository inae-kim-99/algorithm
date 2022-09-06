# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# leetcode 108 : Convert Sorted Array to Binary Search Tree
# LEVEL : Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getChildNode(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None

        mid = (start + end) // 2

        node = TreeNode()
        node.val = nums[mid]
        node.left = self.getChildNode(nums, start, mid-1)
        node.right = self.getChildNode(nums, mid+1, end)

        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getChildNode(nums, 0, len(nums)-1)
