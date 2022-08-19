# https://www.acmicpc.net/problem/1463
# 백준 1463 : 1로 만들기
# LEVEL : Silver 3

import sys


def solution():
    N = int(sys.stdin.readline())

    dp = [N for _ in range(N+1)]
    dp[N] = 0

    for num in range(N, 0, -1):
        if dp[num] != N:
            if num % 3 == 0:
                dp[num//3] = min(dp[num//3], dp[num]+1)
            if num % 2 == 0:
                dp[num//2] = min(dp[num//2], dp[num]+1)
            dp[num-1] = min(dp[num-1], dp[num]+1)

    print(dp[1])


solution()
