# https://www.acmicpc.net/problem/1072
# 백준 1072 : 게임
# LEVEL : Silver 3

import sys

def solution():
    X, Y = map(int, sys.stdin.readline().split())
    current_rate = (Y * 100) // X

    if current_rate >= 99:
        print(-1)
    else:
        start, end = 1, X

        while start <= end:
            mid = (start + end) // 2
            rate = (Y + mid) * 100 // (X + mid)
            
            if rate > current_rate:
                end = mid - 1
            else:
                start = mid + 1
        
        print(end + 1)
        
solution()
