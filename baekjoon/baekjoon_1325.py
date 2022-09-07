# https://www.acmicpc.net/problem/1325
# 백준 1325 : 효율적인 해킹
# LEVEL : Silver 1

import sys
from collections import defaultdict, deque


def solution():
    def bfs(num):
        visited = [False] * (N + 1)
        visited[num] = True

        q = deque([num])
        count = 1

        while q:
            computer = q.popleft()
            for neighbor in graph[computer].keys():
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    q.append(neighbor)
        
        return count
                    
    N, M = map(int, sys.stdin.readline().split())
    graph = defaultdict(dict)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = True

    hackings = []
    max_hacking = 0
    
    for i in range(1, N+1):
        hacking = bfs(i)
        hackings.append((hacking, i))
        max_hacking = max(max_hacking, hacking)

    for hacking, computer in hackings:
        if hacking == max_hacking:
            print(computer, end=' ')


solution()

    
