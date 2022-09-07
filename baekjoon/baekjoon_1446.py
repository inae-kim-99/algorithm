# https://www.acmicpc.net/problem/1446
# 백준 1446 : 지름길
# LEVEL : Silver 1

import sys
from collections import defaultdict
import heapq

def solution():
    N, D = map(int, sys.stdin.readline().split()) # N:지름길개수, D:고속도로길이
    roads = defaultdict(dict)
    fast_destination = []

    for _ in range(N): # {지름길 시작위치 : {도착위치1:거리1, 도착위치2:거리, ...}}
        start, end, weight = map(int, sys.stdin.readline().split())
        roads[start][end] = min(roads[start].get(end, float("inf")), weight)
        fast_destination.append(end) # 지름길 도착 위치를 따로 저장

    memo = [i for i in range(10001)]

    for start in range(D+1):
        # 현재 위치 전에 지름길이 존재할 때
        for destination in fast_destination:
            if destination <= start:
                memo[start] = min(memo[start], memo[destination] + (start-destination)) # 지름길을 거쳐오는 길이의 최솟값을 저장

        # 현재 위치부터 시작하는 지름길이 존재할 때
        for end, length in roads[start].items():
            memo[end] = min(memo[end], memo[start] + length) # 지름길의 도착 위치에 최솟값을 저장

    print(memo[D])


def solution_dijkstra():
    N, D = map(int, sys.stdin.readline().split())  # N:지름길개수, D:고속도로길이
    # {지름길 시작위치 : {도착위치1:거리1, 도착위치2:거리, ...}}
    graph = {i: {i+1: 1} for i in range(D+1)}
    distance = [sys.maxsize] * (D+1)
    distance[0] = 0

    for _ in range(N): 
        start, end, length = map(int, sys.stdin.readline().split())
        if end <= D:
            graph[start][end] = length

    queue = []
    heapq.heappush(queue, (0, 0))
    
    while queue:
        start, length = heapq.heappop(queue)
        
        if length > distance[start]:
            continue

        for end, next_length in graph[start].items():
            cost = length + next_length
            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(queue, (end, cost))

    print(distance[D])


solution_dijkstra()
