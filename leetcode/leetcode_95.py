# https://leetcode.com/problems/unique-binary-search-trees-ii/
# leetcode 95 : Unique Binary Search Trees II
# LEVEL : Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTree(self, start, end):
        trees = []

        if start > end:
            trees.append(None)
            return trees
        elif start == end:
            trees.append(TreeNode(start))
            return trees
        
        for i in range(start, end+1):
            left_nodes = self.generateTree(start, i-1)
            right_nodes = self.generateTree(i+1, end)

            for left in left_nodes:
                for right in right_nodes:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    trees.append(root)

        return trees


    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateTree(1, n)
