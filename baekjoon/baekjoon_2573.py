# https://www.acmicpc.net/problem/2573
# 백준 2573 : 빙산
# LEVEL : Gold 4

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    
    DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def get_sub_iceberg_size():
        size = 1
        visited = [[False for _ in range(M)] for _ in range(N)]

        for y in range(1, N-1):
            for x in range(1, M-1):
                if area[y][x] > 0:
                    queue = deque([(y, x)])
                    visited[y][x] = True

                    while queue:
                        cy, cx = queue.popleft()

                        for dy, dx in DIRECTIONS:
                            ny = cy + dy
                            nx = cx + dx
                            if area[ny][nx] > 0 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                size += 1
                                queue.append((ny, nx))
                    
                    return size
        
        return 0

    def decrease_and_get_iceberg_num():
        decreasing = []
        iceberg = 0
        for y in range(1, N-1):
            for x in range(1, M-1):
                if area[y][x] > 0:
                    water = 0
                    for dy, dx in DIRECTIONS:
                        water += (1 if area[y+dy][x+dx] <= 0 else 0)

                    decreasing.append((y, x, water))

                    if area[y][x] - water > 0:
                        iceberg += 1
        
        for y, x, water in decreasing:
            area[y][x] -= water
        
        return iceberg

    year = 1
    while True:
        iceberg = decrease_and_get_iceberg_num()
        
        if get_sub_iceberg_size() < iceberg:
            print(year)
            break
        
        if iceberg == 0:
            print(0)
            break

        year += 1


solution()
