# https://www.acmicpc.net/problem/2141
# 백준 2141 : 우체국
# LEVEL : Gold 4

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    town = []
    total = 0

    for _ in range(N):
        location, number = map(int, input().split())
        town.append((location, number))
        total += number

    town.sort(key=lambda x: x[0])

    half = 0
    target = total / 2
    for location, number in town:
        half += number
        if half >= target:
            print(location)
            break

solution()