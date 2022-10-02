# https://www.acmicpc.net/problem/17404
# 백준 17404 : RGB거리 2
# LEVEL : Gold 4

import sys
input = sys.stdin.readline

def solution():
    INF = float('inf')
    
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    answer = INF

    for k in range(3):
        dp = [[INF, INF, INF] for _ in range(N)]
        dp[0][k] = cost[0][k]

        for i in range(1, N):
            dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

        for j in range(3):
            if k != j:
                answer = min(answer, dp[-1][j])

    print(answer)
    

solution()