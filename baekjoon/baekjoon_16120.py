# https://www.acmicpc.net/problem/16120
# 백준 1260 : PPAP
# LEVEL : Gold 4

import sys


def solution():
    p = sys.stdin.readline().rstrip()

    stack = []
    for i in range(len(p)):
        stack.append(p[i])
        if stack[-4:] == ['P', 'P', 'A', 'P']:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ['P']:
        print("PPAP")
    else:
        print("NP")


solution()
