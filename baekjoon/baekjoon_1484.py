# https://www.acmicpc.net/problem/1484
# 백준 1484 : 다이어트
# LEVEL : Gold 5

import sys

def solution():
    G = int(sys.stdin.readline())

    answer = []

    now = 2
    before = 1

    while True:
        diff = now*now - before*before

        if before + 1 == now and diff > G:
            break

        if diff == G:
            answer.append(now)
            before += 1
            now += 1
        elif diff > G:
            before += 1
        else:
            now += 1
        
    if not answer:
        print(-1)
    else:
        for a in answer:
            print(a)


solution()
