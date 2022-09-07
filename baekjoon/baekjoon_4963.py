# https://www.acmicpc.net/problem/4963
# 백준 4963 : 섬의 개수 
# LEVEL : Silver 2

import sys
from collections import deque

def solution():
    direct_x = [-1, 0, 1]
    direct_y = [-1, 0, 1]

    while True:
        width, height = map(int, sys.stdin.readline().split())

        if width == 0 and height == 0: # 입력 종료 조건
            return
        
        area = [list(map(int, sys.stdin.readline().split())) for _ in range(height)] # 지도
        
        ans = 0

        for i in range(height):
            for j in range(width):
                if area[i][j] == 1: # 섬을 발견한 경우
                    q = deque([(i, j)])
                    while q: # i, j 위치와 이어진 정사각형을 모두 0(바다)로 바꿈
                        y, x = q.popleft()

                        if area[y][x] == 0:
                            continue

                        area[y][x] = 0

                        for dy in direct_y: # i,j와 이곳을 둘러싼 8곳을 탐색. 자기 자신은 0(바다)로 바꿨으므로 append 되지 않음
                            for dx in direct_x:
                                ny = y + dy
                                nx = x + dx
                                if 0 <= ny < height and 0 <= nx < width and area[ny][nx] == 1:
                                    q.append((ny, nx))
                    
                    ans += 1
        
        print(ans)


solution()



