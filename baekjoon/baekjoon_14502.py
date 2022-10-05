# https://www.acmicpc.net/problem/14502
# 백준 14502 : 연구소
# LEVEL : Gold 4

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def solution():
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    N, M = map(int, input().split())
    maps = [input().rstrip().split() for _ in range(N)]

    empty_list = []
    virus_list = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == '0':
                empty_list.append((i, j))
            elif maps[i][j] == '2':
                virus_list.append((i, j))
    empty_num = len(empty_list)

    combination_list = combinations(empty_list, 3)
    max_size = 0

    for combination in combination_list:
        for y, x in combination:
            maps[y][x] = '1'

        queue = deque(virus_list)
        visited = [[False for _ in range(M)] for _ in range(N)]
        virus = 0

        while queue:
            y, x = queue.popleft()

            for dy, dx in direction:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == '0' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    virus += 1
                    queue.append((ny, nx))

        max_size = max(empty_num - 3 - virus, max_size)

        for y, x in combination:
            maps[y][x] = '0'

    print(max_size)


solution()
