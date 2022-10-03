# https://www.acmicpc.net/problem/9205
# 백준 9205 : 맥주 마시면서 걸어가기
# LEVEL : Silver 1

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def solution():
    LIMIT = 20 * 50

    TC = int(input())

    for _ in range(TC):
        N = int(input())
        location = [list(map(int, input().split())) for _ in range(N+2)]

        graph = defaultdict(dict)

        for i in range(len(location)-1):
            start_y, start_x = location[i][1], location[i][0]
            for j in range(i+1, len(location)):
                end_y, end_x = location[j][1], location[j][0]
                if abs(start_y-end_y) + abs(start_x-end_x) <= LIMIT:
                    graph[i][j] = True
                    graph[j][i] = True
        
        queue = deque([0])
        visited = [False for _ in range(N+2)]
        result = "sad"

        while queue:
            node = queue.popleft()

            if node == N+1:
                result = "happy"
                break
                
            for next_node in graph[node].keys():
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
        
        print(result)


solution()