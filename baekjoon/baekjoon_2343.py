# https://www.acmicpc.net/problem/2343
# 백준 2343 : 기타 레슨
# LEVEL : Silver 1

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    times = list(map(int, input().split())) 
    max_time = max(times)

    start = 0
    end = sum(times)

    answer = float('inf')

    while start <= end:
        mid = (start + end) // 2

        if mid < max_time:
            start = mid + 1
            continue

        bluray = 1
        length = 0
        for i in range(N):
            if length + times[i] <= mid:
                length += times[i]
            else:
                bluray += 1
                length = times[i]

        if bluray <= M:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    print(answer)
   

solution()