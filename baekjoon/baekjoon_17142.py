# https://www.acmicpc.net/problem/17142
# 백준 17142 : 연구소 3
# LEVEL : Gold 4

from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def solution():
    EMPTY = '0'
    WALL = '1'
    VIRUS = '2'
    DIRECTION = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    N, M = map(int, input().split())
    area = [input().rstrip().split() for _ in range(N)] # 맵
    times = [] # 각 경우마다 걸리는 시간을 저장

    virus_locations = []
    wall_cnt = 0

    for i in range(N):
        for j in range(N):
            if area[i][j] == VIRUS:
                virus_locations.append((i, j, 0)) # virus를 놓을 수 있는 위치 저장
            elif area[i][j] == WALL:
                wall_cnt += 1 # 벽 개수 카운트

    empty_cnt = N * N - wall_cnt - len(virus_locations) # 빈 공간의 개수 카운트

    if empty_cnt == 0: # 만약 빈 공간이 없으면 바로 0 출력
        print(0)
        return

    for viruses in list(combinations(virus_locations, M)): # virues를 놓을 수 있는 위치를 M개 선택한다.
        visited = [[False for _ in range(N)] for _ in range(N)]
        queue = deque(viruses)

        cnt = 0
        while queue:
            y, x, t = queue.popleft() # y, x : 현재 바이러스의 위치, t : 이 위치까지 오는 데 걸린 시간

            for dy, dx in DIRECTION:
                ny = y + dy
                nx = x + dx

                if 0 <= ny < N and 0 <= nx < N and \
                        area[ny][nx] != WALL and not visited[ny][nx]:
                    
                    visited[ny][nx] = True
                    queue.append((ny, nx, t + 1))

                    if area[ny][nx] == EMPTY: # 빈 공간에 바이러스가 복제된 경우
                        cnt += 1

            if cnt >= empty_cnt: # 빈 공간에 모두 바이러스가 복제된 경우
                times.append(t+1)
                break

    if times:
        print(min(times))
    else:
        print(-1)

    
solution()
