# https://leetcode.com/problems/number-of-1-bits/
# leetcode 191 : Number of 1 Bits
# LEVEL : Easy
#
# n이 0이 될때까지 n & (n-1) 계산을 반복한다.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            count += 1
            n = n & (n-1)

        return count