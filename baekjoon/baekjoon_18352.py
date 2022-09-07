`# https://www.acmicpc.net/problem/18352
# 백준 : 183512 : 특정 거리의 도시 찾기
# LEVEL : Silver 2

import sys
import heapq

def solution():
    N, M, K, X = map(int, sys.stdin.readline().split())
    graph = {i+1:{} for i in range(N)}

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        graph[start][end] = True

    distance = {node:float('inf') for node in graph}
    distance[X] = 0

    queue = []
    heapq.heappush(queue, [distance[X], X])

    while queue:
        curr_distance, curr_location = heapq.heappop(queue)

        if curr_distance > distance[curr_location]:
            continue

        for next_location in graph[curr_location].keys():
            next_distance = curr_distance + 1
            if next_distance < distance[next_location]:
                distance[next_location] = next_distance
                heapq.heappush(queue, [next_distance, next_location])
    
    if K in distance.values():
        for location, dist in distance.items():
            if dist == K:
                print(location)
    else:
        print(-1)

solution()



`