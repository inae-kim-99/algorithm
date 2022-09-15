# https://www.acmicpc.net/problem/9084
# baekjoon 9084 : 동전
# LEVEL : Gold 5

import sys

def solution():
    T = int(sys.stdin.readline())

    for _ in range(T):

        N = int(sys.stdin.readline())  # 동전의 종류 수
        coins = list(map(int, sys.stdin.readline().split())) # 동전 금액들
        target = int(sys.stdin.readline())  # 만들어야 하는 금액
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(target + 1):
                if i >= coin:
                    dp[i] += dp[i-coin]
        
        print(dp[target])


solution()
