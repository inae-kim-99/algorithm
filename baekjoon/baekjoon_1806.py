# https://www.acmicpc.net/problem/1806
# 백준 1806 : 부분합
# LEVEL : Gold 4

import sys
input = sys.stdin.readline


def solution():
    N, S = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(N-1):
        nums[i+1] += nums[i]

    start = 0
    distance = N + 1

    for end in range(N):
        while nums[end] - nums[start] >= S:
            start += 1
        if nums[end] >= S:
            distance = min(distance, end-start+1)
    
    if distance == N + 1:
        distance = 0

    print(distance)


solution()
