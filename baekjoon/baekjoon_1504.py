# https://www.acmicpc.net/problem/1504
# 백준 1504 : 특정한 최단 경로
# LEVEL : Gold 4

import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline


def solution():
    INF = float('inf')

    N, E = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    v1, v2 = map(int, input().split())

    def dijkstra(start):
        distance = [INF for _ in range(N+1)]
        distance[start] = 0

        queue = [(0, start)]
        while queue:
            curr_cost, curr_node = heapq.heappop(queue)

            if curr_cost > distance[curr_node]:
                continue

            for next_node, next_cost in graph[curr_node].items():
                cost = curr_cost + next_cost
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(queue, (cost, next_node))

        return distance

    s_dist = dijkstra(1)
    v1_dist = dijkstra(v1)
    v2_dist = dijkstra(v2)

    answer = min(s_dist[v1] + v1_dist[v2] + v2_dist[N],
                 s_dist[v2] + v2_dist[v1] + v1_dist[N])
    
    if answer == INF:
        answer = -1

    print(answer)


solution()
