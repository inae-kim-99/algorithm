# https://www.acmicpc.net/problem/11725
# 백준 11725 : 트리의 부모 찾기
# LEVEL : Silver 2

import sys
from collections import defaultdict, deque

def solution():
    N = int(sys.stdin.readline())
    edges = defaultdict(dict)
    parents = [-1 for _ in range(N+1)]

    for _ in range(N-1):
        first, second = map(int, sys.stdin.readline().split())
        edges[first][second] = True
        edges[second][first] = True

    queue = deque([(1, 0)])

    while queue:
        node, parent = queue.popleft()

        parents[node] = parent
        
        for child in edges[node].keys():
            if child != parent:
                queue.append((child, node))

    for i in range(2, N+1):
        print(parents[i])


solution()

