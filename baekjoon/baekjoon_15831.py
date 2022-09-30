# https://www.acmicpc.net/problem/15831
# 백준 15831 : 준표의 조약돌
# LEVEL : Gold 4

import sys
input = sys.stdin.readline

def solution():
    N, B, W = map(int, input().split())
    stones = input().rstrip()

    start, end = 0, 0

    count = {'W':0, 'B':0}
    distance = 0

    while end < len(stones):
        count[stones[end]] += 1
        if count['B'] <= B:
            if count['W'] >= W:
                distance = max(distance, end - start + 1)
            end += 1
        else:
            count[stones[start]] -= 1
            start += 1
            end += 1
        
    print(distance)

        
solution()
