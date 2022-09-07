# https://www.acmicpc.net/problem/1654
# 백준 1654 : 랜선 자르기
# LEVEL : Silver 2

import sys

def solution():
    K, N = map(int, sys.stdin.readline().split())
    rows = [int(sys.stdin.readline()) for _ in range(K)]

    rows.sort(reverse=True)

    start = 1
    end = max(rows)

    while start <= end:
        mid = (start + end) // 2

        count = sum([row//mid for row in rows])
        if count >= N:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


solution()
    