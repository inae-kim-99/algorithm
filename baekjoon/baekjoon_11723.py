# https://www.acmicpc.net/problem/11723
# 백준 11723 : 집합
# LEVEL : Silver 4

import sys


def solution():
    N = int(sys.stdin.readline())
    S = 0

    for _ in range(N):
        row = sys.stdin.readline().split()

        command = row[0] # 연산 종류

        number = 0 # 연산할 값 : x
        if len(row) > 1:
            number = int(row[1]) - 1

        if command == 'add':
            S = S | (1 << number)
        elif command == 'remove':
            S = S & ~(1 << number)
        elif command == 'check':
            if S & (1 << number):
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            S = S ^ (1 << number)
        elif command == 'all':
            S = ((1 << 20) - 1)
        elif command == 'empty':
            S = 0


solution()
