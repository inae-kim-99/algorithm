# https://www.acmicpc.net/problem/2240
# 백준 2240 : 자두나무
# LEVEL : Gold 5

import sys
input = sys.stdin.readline

def solution():
    T, W = map(int, input().split())
    trees = [int(input()) for _ in range(T)]

    dp = [[0 for _ in range(W+1)] for _ in range(T+1)]

    for i in range(1, T+1):
        tree = trees[i-1]
        
        # 한 번도 움직이지 않은 경우
        if tree == 1:
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]
        
        # 이동 횟수를 1번부터 W번까지 움직이면서 체크
        for j in range(1, W+1):
            if j > i:
                break

            if (tree == 1 and j % 2 == 0) or (tree == 2 and j % 2 == 1):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
            
    print(max(dp[-1]))


solution()