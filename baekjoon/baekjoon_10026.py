# https://www.acmicpc.net/problem/10026
# 백준 10026 : 적록색약 
# LEVEL : Gold 4

import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input())
    area = [input().rstrip() for _ in range(N)]

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited_same = [[False for _ in range(N)] for _ in range(N)]

    count = 0
    count_same = 0

    def bfs(i, j):
        queue = deque([(i, j)])
        while queue:
            y, x = queue.popleft()

            if visited[y][x]:
                continue

            visited[y][x] = True

            for dy, dx in directions:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < N and \
                    area[i][j] == area[ny][nx] and \
                        not visited[ny][nx]:
                        queue.append((ny, nx))

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count += 1
                dfs(i, j)
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        area[i] = area[i].replace('R','G')
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                count_same += 1
                dfs(i, j)

    print(count, count_same)


solution()
