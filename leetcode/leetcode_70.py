# https://leetcode.com/problems/climbing-stairs/
# leetcode 70 : Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            ways = a + b
            a = b
            b = ways
        return b


Solution.climbStairs(0, 3)
