# https://www.acmicpc.net/problem/2559
# 백준 2559 : 수열
# LEVEL : Silver 3

import sys

def solution():
    N, K = map(int, sys.stdin.readline().split())
    temp = list(map(int, sys.stdin.readline().split()))
    temp.insert(0, 0)

    for i in range(1, N+1):
        temp[i] += temp[i-1]

    answer = (temp[K] - temp[0])

    for i in range(K+1, N+1):
        if (temp[i] - temp[i-K]) > answer:
            answer = (temp[i] - temp[i-K])

    print(answer)


solution()
