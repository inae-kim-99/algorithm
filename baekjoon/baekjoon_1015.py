# https://www.acmicpc.net/problem/1015
# 백준 1015 : 수열 정렬
# LEVEL : Silver 4

import sys

def solution():
    N = int(sys.stdin.readline())

    list_a = list(map(int, sys.stdin.readline().split()))
    index_a = [i for i in range(N)]

    for i in range(N):
        for j in range(N-i-1):
            if list_a[j] > list_a[j+1]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                index_a[j], index_a[j+1] = index_a[j+1], index_a[j]

    for i in range(N):
        if i == N-1:
            print(index_a.index(i), end='')
        else:
            print(index_a.index(i), end=' ')

solution()