# https://www.acmicpc.net/problem/1926
# 백준 1926 : 그림
# LEVEL : Silver 1

import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    paintings = [0]

    def calculate_area(y, x):
        paper[y][x] = 0
        cnt = 1

        q = deque([(y, x)])

        while q:
            check_y, check_x = q.popleft()

            for dy, dx in directions:
                ny = check_y + dy
                nx = check_x + dx
                if 0 <= ny < n and 0 <= nx < m and paper[ny][nx] == 1:
                    paper[ny][nx] = 0
                    cnt += 1
                    q.append((ny, nx))

        return cnt

    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1:
                paintings.append(calculate_area(i, j))

    print(len(paintings)-1)
    print(max(paintings))


solution()
