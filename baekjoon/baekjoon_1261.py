# https://www.acmicpc.net/problem/1261
# 백준 1261 : 알고스팟
# LEVEL : Gold 4

import sys
from collections import deque
input = sys.stdin.readline


def solution():
    INF = float('inf')

    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    M, N = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(N)]
    
    q = deque([(0, 0)])
    distance = [[INF for _ in range(M)] for _ in range(N)]
    distance[0][0] = 0
    
    while q:
        y, x = q.popleft()

        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and distance[ny][nx] == INF:
                if maze[ny][nx] == '1':
                    q.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
                else:
                    q.appendleft((ny, nx))
                    distance[ny][nx] = distance[y][x]

    print(distance[N-1][M-1])


solution()
