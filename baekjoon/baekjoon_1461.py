# https://www.acmicpc.net/problem/1461
# 백준 1461 : 도서관
# LEVEL : Gold 5

import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    books = sorted(list(map(int, sys.stdin.readline().split())))
    distance = 0

    pivot = N
    for i in range(N):
        if books[i] >= 0:
            pivot = i
            break
    
    for i in range(0, pivot, M):
        distance += books[i] * (-2)
    
    for i in range(N-1, pivot-1, -M):
        distance += books[i] * 2

    if abs(books[0]) < abs(books[-1]):
        distance -= abs(books[-1])
    else:
        distance -= abs(books[0])
    
    print(distance)


solution()
