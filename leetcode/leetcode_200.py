# https://leetcode.com/problems/number-of-islands/
# leetcode 200 : Number of Islands
# LEVEL : Medium

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
                return 0

            grid[i][j] = "0"

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += dfs(i, j)

        return islands
