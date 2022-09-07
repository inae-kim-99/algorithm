# https://www.acmicpc.net/problem/2805
# 백준 2805 : 나무 자르기
# LEVEL : Silver 2

import sys

def solution():
    N, M = map(int, sys.stdin.readline().split())

    heights = list(map(int, sys.stdin.readline().split()))

    low, high = 0, max(heights)-1
    while low <= high:
        mid = (low + high) // 2

        height_sum = 0
        for h in heights:
            if h > mid:
                height_sum += (h - mid)
        
        if height_sum >= M:
            low = mid + 1
        else:
            high = mid - 1
    
    print(high)

def solution2():
    N, M = map(int, sys.stdin.readline().split())
    tree = map(int, sys.stdin.readline().split())
    
    for t in tree:
        print(t)

    start = 0
    end = max(tree)-1
    while start <= end:
        mid = (start + end) // 2
        b = [i-mid if i-mid > 0 else 0 for i in tree]
    
        if sum(b) < M:
            end = mid - 1
        elif sum(b) == M:
            start = mid
            break
        else:
            start = mid + 1
    print(start)

solution2()
