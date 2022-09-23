# https://www.acmicpc.net/problem/14497
# 백준 14497 : 주난의 난
# LEVEL : Gold 4

from collections import deque
import sys
input = sys.stdin.readline

def solution():
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    N, M = map(int, input().split())

    start_y, start_x, _, _ = map(int, input().split())
    start_y -= 1
    start_x -= 1

    room = [list(input().rstrip()) for _ in range(N)]

    def jump_and_find():
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[start_y][start_x] = True
        
        queue = deque([(start_y, start_x)])

        while queue:
            y, x = queue.popleft()

            if room[y][x] == '#':
                return True

            for dy, dx in DIRECTIONS:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if room[ny][nx] == '1':
                         room[ny][nx] = '0'
                    else:
                        queue.append((ny, nx))
        
        return False
                     
    count = 1
    while jump_and_find() == False:
        count += 1
        
    print(count)


solution()
