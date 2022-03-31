# https://leetcode.com/problems/counting-bits/
# leetcode 338 : Counting Bits
# LEVEL : Easy

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            result[i] = result[i-(i & -i)]+1

        return result
