# https://www.acmicpc.net/problem/19638
# 백준 19638 : 센티와 마법의 뿅망치
# LEVEL : Silver 1

import sys
from heapq import heappop, heappush, heapify

def solution():
    N, H, T = map(int, sys.stdin.readline().split())
    heights = [-int(sys.stdin.readline()) for _ in range(N)]

    heapify(heights) # 최대힙 큐로 변환

    if -heights[0] < H:
        print("YES")
        print(0)
        return

    for i in range(T):
        height = int(heappop(heights) / 2)

        if height == 0:
            height = -1

        heappush(heights, height)
        
        if -heights[0] < H:
            print("YES")
            print(i+1)
            break
    else:
        print("NO")
        print(-heights[0])
    

solution()
