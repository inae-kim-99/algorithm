# https://www.acmicpc.net/problem/1753
# 백준 1753 : 최단경로
# LEVEL : Gold 4

import sys
import heapq


def solution():
    INF = float('inf')
    V, E = map(int, sys.stdin.readline().split())
    start = int(sys.stdin.readline()) - 1
    distances = [INF] * V

    graph = [[] for _ in range(V)]
    for _ in range(E):
        s, e, w = map(int, sys.stdin.readline().split())
        graph[s-1].append((e-1, w))

    def dijkstra(start):
        queue = []
        heapq.heappush(queue, (0, start))
        distances[start] = 0

        while queue:
            curr_distance, curr_destination = heapq.heappop(queue)

            if curr_distance > distances[curr_destination]:
                continue

            for new_destination, new_distance in graph[curr_destination]:
                distance = curr_distance + new_distance
                if distance < distances[new_destination]:
                    distances[new_destination] = distance
                    heapq.heappush(queue, (distance, new_destination))

    dijkstra(start)

    for d in distances:
        print(d if d != INF else "INF")


solution()
