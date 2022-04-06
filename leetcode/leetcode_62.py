# https://leetcode.com/problems/unique-paths/
# leetcode 62 : Unique Paths
# LEVEL : Medium

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            for i in range(1, n):
                row[i] += row[i-1]
                            
        return row[n-1]