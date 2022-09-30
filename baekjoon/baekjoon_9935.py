# https://www.acmicpc.net/problem/9935
# 백준 9935 : 문자열 폭발
# LEVEL : Gold 4

import sys
input = sys.stdin.readline

def solution():
    word = input().rstrip()
    target = list(input().rstrip())
    target_len = len(target)

    arr = []
    for i in range(len(word)):
        arr.append(word[i])

        if arr[-target_len:] == target:
            for _ in range(target_len):
                arr.pop()

    if arr:
        print("".join(arr))
    else:
        print("FRULA")


solution()
