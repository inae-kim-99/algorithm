# https://www.acmicpc.net/problem/12865
# 백준 12865 : 평범한 배낭
# LEVEL : Gold 5

import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    stuff = [[0, 0]]
    for _ in range(N):
        stuff.append(list(map(int, input().split())))

    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N+1): # i : 물건 종류
        weight, value = stuff[i]
        for j in range(K+1): # j : 현재 무게
            if j < weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
    
    print(dp[N][K])

solution()