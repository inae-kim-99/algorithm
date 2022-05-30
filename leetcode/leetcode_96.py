# https://leetcode.com/problems/unique-binary-search-trees/
# leetcode 96 : Unique Binary Search Trees
# LEVEL : Medium

class Solution:
    def numTrees(self, n: int) -> int:
        if n < 3:
            return n
        
        tree = [0] * (n+1)
        tree[0], tree[1], tree[2] = 1, 1, 2
        
        for i in range(3, n+1):
            tree[i] = sum([tree[j-1] * tree[i-j] for j in range(1, i+1)])
            
        return tree[n]