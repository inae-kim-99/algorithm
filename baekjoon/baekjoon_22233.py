# https://www.acmicpc.net/problem/22233
# baekjoon 22233 : 가희와 키워드
# LEVEL : Silver 2

import sys
from collections import defaultdict

def solution():
    [N, M] = list(map(int, sys.stdin.readline().rstrip().split()))

    memo = defaultdict(int)
    count = N

    for _ in range(N):
        memo[sys.stdin.readline().rstrip()] += 1

    for _ in range(M):
        keywords = sys.stdin.readline().rstrip().split(',')

        for keyword in keywords:
            if memo[keyword] > 0:
                memo[keyword] -= 1
                count -= 1
        print(count)

solution()