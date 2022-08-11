# https://www.acmicpc.net/problem/13549
# 백준 13549 : 숨바꼭질 3
# LEVEL : Gold 5
import sys
from collections import deque, defaultdict

def solution():
    [N, K] = list(map(int, sys.stdin.readline().rstrip().split()))
        
    dq = deque([N])
    visited = [-1 for _ in range(100001)]
    visited[N] = 0

    while dq:
        loc = dq.popleft()
        
        if loc == K:
            print(visited[loc])
            break

        if 0 <= loc-1 < 100001 and visited[loc-1] == -1:
            visited[loc-1] = visited[loc]+1
            dq.append(loc-1)
        if 0 < loc*2 < 100001 and visited[loc*2] == -1:
            visited[loc*2] = visited[loc]
            dq.appendleft(loc*2)
        if 0 <= loc+1 < 100001 and visited[loc+1] == -1:
            visited[loc+1] = visited[loc]+1
            dq.append(loc+1)
        

solution()
        

