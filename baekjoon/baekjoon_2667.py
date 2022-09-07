# https://www.acmicpc.net/problem/2667
# 백준 2667 : 단지번호붙이기
# LEVEL : Silver 1

import sys
from collections import deque


def solution():
    N = int(sys.stdin.readline())
    area = [list(sys.stdin.readline().rstrip())
            for _ in range(N)]
    
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 탐색할 방향

    homes = [] # 각 단지에 속하는 집의 수를 저장하는 리스트
    count_total = 0 # 단지 수

    for i in range(N):
        for j in range(N):
            if area[i][j] == '1':
                count_home = 0
                q = deque([(i, j)])
                while q:
                    y, x = q.popleft()

                    if area[y][x] == '0':
                        continue

                    area[y][x] = '0'
                    count_home += 1

                    for dy, dx in directions: # 상하좌우 탐색
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < N and 0 <= nx < N and area[ny][nx] == '1':
                            q.append((ny, nx))

                homes.append(count_home)
                count_total += 1

    print(count_total)
    for home in sorted(homes):
        print(home)


solution()

    
