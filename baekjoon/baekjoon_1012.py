# https://www.acmicpc.net/problem/1012
# 백준 1012 : 유기농 배추
# LEVEL : Silver 2

import sys
from collections import deque

def solution():
    direction = [(0,1),(0,-1),(1,0),(-1,0)]

    T = int(sys.stdin.readline())

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        field = [[False for _ in range(M)] for _ in range(N)]
        visited = [[False for _ in range(M)] for _ in range(N)]

        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split())
            field[y][x] = True
        
        count = 0

        for y in range(N):
            for x in range(M):
                if field[y][x] and not visited[y][x]:
                    count += 1

                    dq = deque([(y, x)])
                    visited[y][x] = True

                    while dq:
                        loc_y, loc_x = dq.popleft()

                        for dy, dx in direction:
                            ny, nx = loc_y+dy, loc_x+dx
                            if 0 <= ny < N and 0 <= nx < M and \
                                field[ny][nx] and not visited[ny][nx]:
                                visited[ny][nx] = True
                                dq.append((ny, nx))
        
        print(count)


solution()

