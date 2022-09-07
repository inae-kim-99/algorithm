# https://leetcode.com/problems/beautiful-arrangement/
# leetcode 526 : Beautiful Arrangement
# LEVEL : Medium

class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(i):
            if i == 0:
                self.ans += 1
                return
            for j in range(1, n+1):
                if not visited[j] and (j % i == 0 or i % j == 0):
                    visited[j] = True
                    dfs(i-1)
                    visited[j] = False

        self.ans = 0
        visited = [False]*(n+1)
        dfs(n)
        return self.ans
