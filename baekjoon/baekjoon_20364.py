# https://www.acmicpc.net/problem/20364
# 백준 20364 : 부동산 다툼
# LEVEL : Silver 2

import sys

def solution():
    N, Q = map(int, sys.stdin.readline().split())
    nums = [int(sys.stdin.readline()) for _ in range(Q)]
    
    visited = [False] * (N+1)

    for i in range(Q):
        answer = 0
        target = nums[i]
        while target:
            if visited[target]:
                answer = target
            target //= 2
        
        if answer == 0:
            visited[nums[i]] = True

        print(answer)


solution()