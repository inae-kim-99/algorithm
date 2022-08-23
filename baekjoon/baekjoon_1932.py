# https://www.acmicpc.net/problem/1932
# 백준 1932 : 정수 삼각형
# LEVEL : Silver 2
import sys


def solution():
    N = int(sys.stdin.readline())
    triangle = [list(map(int, sys.stdin.readline().split()))
                for _ in range(N)]

    for floor in range(1, N):
        for i in range(floor+1):
            if i == 0:
                triangle[floor][i] += triangle[floor-1][i]
            elif i == floor:
                triangle[floor][i] += triangle[floor-1][i-1]
            else:
                triangle[floor][i] += max(triangle[floor-1]
                                          [i-1], triangle[floor-1][i])

    print(max(triangle[N-1]))


solution()
