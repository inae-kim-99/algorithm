# https://www.acmicpc.net/problem/1495
# 백준 1495 : 기타리스트
# LEVEL : Silver 1

import sys

def solution():
    N, S, M = map(int, sys.stdin.readline().split())

    diff = list(map(int, sys.stdin.readline().split()))

    volumes = [[] for _ in range(N+1)]
    volumes[0].append(S)
    volumes[N].append(-1)

    for i in range(N):
        for before_volume in volumes[i]:
            if before_volume - diff[i] >= 0:
                volumes[i+1].append(before_volume - diff[i])
            if before_volume + diff[i] <= M:
                volumes[i+1].append(before_volume + diff[i])

    print(max(volumes[N]))


solution()