# https://www.acmicpc.net/problem/4485
# 백준 4485 : 녹색 옷 입은 애가 젤다지?
# LEVEL : Gold 4

import sys
from collections import deque
from heapq import heappop, heappush

def dijkstra(n, graph, cost, y, x):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    pq = []

    heappush(pq, (graph[y][x], y, x))
    while pq:
        curr_cost, curr_y, curr_x = heappop(pq)

        if cost[curr_y][curr_x] < curr_cost:
            continue

        for dy, dx in direction:
            ny, nx = curr_y + dy, curr_x + dx
            if 0 <= ny < n and 0 <= nx < n:
                next_cost = curr_cost + graph[ny][nx]
                if next_cost < cost[ny][nx]:
                    heappush(pq, (next_cost, ny, nx))
                    cost[ny][nx] = next_cost 

    return cost[n-1][n-1]

def solution():
    tc = 1
    while True:
        N = int(sys.stdin.readline().rstrip())
        if N == 0:
            break

        graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
        cost = [[int(1e5)] * N for _ in range(N)]

        answer = dijkstra(N, graph, cost, 0, 0)
    
        print(f"Problem {tc}: {answer}")
        tc += 1


solution()
