# https://www.acmicpc.net/problem/19598
# 백준 19598 : 최소 회의실 개수
# LEVEL : Gold 5

import sys
from heapq import heappop, heappush

def solution():
    N = int(sys.stdin.readline().rstrip())
    times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    times.sort(key=lambda x : (x[0], x[1]))
    rooms = [0]

    for start, end in times:
        room = heappop(rooms)
        if room > start:
            heappush(rooms, room)
        heappush(rooms, end)

    print(len(rooms))
        

solution()
