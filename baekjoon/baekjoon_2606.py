# https://www.acmicpc.net/problem/2606
# 백준 2606 : 바이러스
# LEVEL : Silver 3

import sys
from collections import deque

def solution():
    computer_num = int(sys.stdin.readline())
    pair_num = int(sys.stdin.readline())

    graph = [[False for _ in range(computer_num)] for _ in range(computer_num)]
    visited = [False for _ in range(computer_num)]

    for _ in range(pair_num):
        c1, c2 = map(int, sys.stdin.readline().split())
        graph[c1-1][c2-1] = True
        graph[c2-1][c1-1] = True

    def dfs(com):
        if visited[com]:
            return
        
        visited[com] = True

        for i in range(computer_num):
            if graph[com][i]:
                dfs(i)
    
    dfs(0)
    print(visited.count(True)-1)

solution()