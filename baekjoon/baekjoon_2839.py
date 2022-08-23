# https://www.acmicpc.net/problem/2839
# 백준 2839 : 설탕 배달
# LEVEL : Silver 4

import sys


def solution():
    MAX_NUM = 5000

    N = int(sys.stdin.readline())
    dp = [MAX_NUM] * (N+1)
    dp[N] = 0

    for num in range(N, 2, -1):
        if num >= 5:
            dp[num-5] = min(dp[num-5], dp[num] + 1)
        dp[num-3] = min(dp[num-3], dp[num]+1)

    if dp[0] == MAX_NUM:
        print("-1")
    else:
        print(dp[0])


def solution2():
    N = int(sys.stdin.readline())
    count = 0

    while N >= 0:
        if N % 5 == 0:
            count += (N//5)
            print(count)
            break
        N -= 3
        count += 1
    else:
        print(-1)


solution2()
