# https://www.acmicpc.net/problem/1388
# 백준 1388 : 바닥 장식
# LEVEL : Silver 3

import sys

def solution():
    direct = {'-': [0, 1], '|': [1, 0]}
    VISITED = '.'

    N, M = map(int, sys.stdin.readline().split())
    floor = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(M):
            if floor[i][j] != VISITED:
                ans += 1

                shape = floor[i][j]
                next_y, next_x = i, j
                
                while 0 <= next_y < N and 0 <= next_x < M and \
                    floor[next_y][next_x] == shape:
                    floor[next_y][next_x] = VISITED
                    next_y += direct[shape][0]
                    next_x += direct[shape][1]
            
    print(ans)

solution()


