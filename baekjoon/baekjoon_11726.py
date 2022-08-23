# https://www.acmicpc.net/problem/11726
# 백준 11726 : 2xn 타일링
# LEVEL : Silver
import sys


def solution():
    N = int(sys.stdin.readline())

    memo = [0] * (N+1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2, N+1):
        memo[i] = memo[i-1] + memo[i-2]

    print(memo[N] % 10007)


solution()
