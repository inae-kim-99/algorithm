# https://www.acmicpc.net/problem/2589
# 백준 2589 : 보물섬
# LEVEL : Gold 5

import sys
from collections import deque
input = sys.stdin.readline

def solution():
    direction = [[1,0], [-1, 0], [0, 1], [0, -1]]

    row, col = map(int, input().split())
    area = [list(input().rstrip()) for _ in range(row)]

    def count_neighbor(y, x):
        count = 0
        for dy, dx in direction:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < row and 0 <= nx < col and area[ny][nx] == 'L':
                count += 1
        return count

    def bfs(y, x):
        distance = 0

        visited = [[0 for _ in range(col)] for _ in range(row)]
        visited[y][x] = 1

        q = deque([(y, x)])

        while q:
            curr_y, curr_x = q.popleft()

            for dy, dx in direction:
                ny = curr_y + dy
                nx = curr_x + dx
                if 0 <= ny < row and 0 <= nx < col and area[ny][nx] == 'L' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[curr_y][curr_x] + 1
                    if visited[ny][nx] > distance:
                        distance = visited[ny][nx]
                    q.append((ny, nx))
            
        return distance - 1


    answer = 0

    for i in range(row):
        for j in range(col):
            if area[i][j] == 'L' and count_neighbor(i, j) <= 2:
                time = bfs(i, j)
                if time > answer:
                    answer = time
        
    print(answer)


solution()