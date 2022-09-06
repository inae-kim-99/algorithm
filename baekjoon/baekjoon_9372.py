# https://www.acmicpc.net/problem/9372
# 백준 9372 : 상근이의 여행
# LEVEL : Silver 4

import sys
from collections import defaultdict, deque
from this import d


def solution():
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        airlines = defaultdict(dict)
        visited = [False for _ in range(N+1)]
        visited[1] = True

        for _ in range(M):
            a, b = map(int, sys.stdin.readline().split())
            airlines[a][b] = True
            airlines[b][a] = True

        queue = deque([1])
        ans = 0
        while queue:
            country = queue.popleft()

            for destination in airlines[country].keys():
                if not visited[destination]:
                    visited[destination] = True
                    ans += 1
                    queue.append(destination)

        print(ans)


def solution2():
    T = int(sys.stdin.readline())

    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        for _ in range(M):
            a, b = map(int, sys.stdin.readline().split())
        print(N-1)

solution2()
# solution()
