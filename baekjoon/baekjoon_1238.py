# https://www.acmicpc.net/problem/1238
# 백준 1238 : 파티
# LEVEL : Gold 3

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def solution():
    INF = float('inf')

    N, M, X = map(int, input().split())
    X = X - 1
    graph = defaultdict(dict)
    answer = [0 for _ in range(N)]
    
    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a-1][b-1] = t

    for i in range(N):
        graph[i][i] = 0

    for i in range(N):
        distance = [INF for _ in range(N)]
        distance[i] = 0

        queue = [(0, i)]

        while queue:
            curr_cost, curr_node = heapq.heappop(queue)

            if curr_cost > distance[curr_node]:
                continue
                
            for adj_node, adj_cost in graph[curr_node].items():
                next_cost = curr_cost + adj_cost
                if distance[adj_node] > next_cost:
                    distance[adj_node] = next_cost
                    heapq.heappush(queue, (next_cost, adj_node))
        
        if i != X:
            answer[i] += distance[X]
        else:
            for j in range(N):
                answer[j] += distance[j]

    max_distance = 0
    for i in range(N):
        max_distance = max(max_distance, answer[i])

    print(max_distance)


solution()