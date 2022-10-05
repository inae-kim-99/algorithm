# https://www.acmicpc.net/problem/14500
# 백준 14500 : 테크로미노
# LEVEL : Gold 4

import sys
input = sys.stdin.readline
answer = 0

def solution():
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False for _ in range(M)] for _ in range(N)]
    max_value = max(map(max, maps))

    def dfs(y, x, count, value):
        global answer
        now_max = value + max_value * (4 - count)

        if now_max <= answer:
            return

        if count == 4:
            answer = max(answer, value)
            return
        
        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if count == 2:
                    visited[ny][nx] = True
                    dfs(y, x, count + 1, value + maps[ny][nx])
                    visited[ny][nx] = False

                visited[ny][nx] = True
                dfs(ny, nx, count + 1, value + maps[ny][nx])
                visited[ny][nx] = False
    

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, maps[i][j])
            visited[i][j] = False
    
    print(answer)


solution()
