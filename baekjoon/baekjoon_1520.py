# https://www.acmicpc.net/problem/1520
# 백준 1520 : 내리막 길
# LEVEL : Gold 3

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution():
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    M, N = map(int, input().split()) # 세로크기, 가로크기
    area = [list(map(int, input().split())) for _ in range(M)]

    dp = [[-1 for _ in range(N)] for _ in range(M)]

    def dfs(y, x):
        if y == M-1 and x == N-1:
            return 1

        if dp[y][x] != -1:
            return dp[y][x]

        dp[y][x] = 0
        
        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < M and 0 <= nx < N and area[ny][nx] < area[y][x]:
                dp[y][x] += dfs(ny, nx)
        
        return dp[y][x]

    
    print(dfs(0, 0))

solution()
