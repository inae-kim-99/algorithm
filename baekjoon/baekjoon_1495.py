# https://www.acmicpc.net/problem/1495
# 백준 1495 : 기타리스트
# LEVEL : Silver 1

import sys

def solution():
    N, S, M = map(int, sys.stdin.readline().split())
    difference = list(map(int, sys.stdin.readline().split()))

    dp = [[False for _ in range(M+1)] for _ in range(N+1)]
    dp[0][S] = True

    for i in range(1, N+1):
        volume = difference[i-1]
        for j in range(M+1):
            if dp[i-1][j]:
                if j - volume >= 0:
                    dp[i][j-volume] = True
                if j + volume <= M:
                    dp[i][j+volume] = True
    
    result = -1
    for i in range(M, -1, -1):
        if dp[N][i]:
            result = i
            break

    print(result)


solution()
