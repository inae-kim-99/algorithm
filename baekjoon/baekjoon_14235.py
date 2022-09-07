# https://www.acmicpc.net/problem/14235
# 백준 14235 : 크리스마스 선물
# LEVEL : Silver 3

import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())
    rows = [input().rstrip() for _ in range(N)]
    q = []

    for row in rows:
        if row == "0":
            if q:
                print(-heapq.heappop(q))
            else:
                print("-1")
        else:
            values = list(map(int, row.split()[1:]))
            for value in values:
                heapq.heappush(q, -value)


solution()