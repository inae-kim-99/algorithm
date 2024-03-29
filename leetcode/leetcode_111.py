# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# leetcode 111 : Minimum Depth of Binary Tree
# LEVEL : Easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = 1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node.left and not node.right:
                    return ans

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
