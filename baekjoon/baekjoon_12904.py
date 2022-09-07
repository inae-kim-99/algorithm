# https://www.acmicpc.net/problem/12904
# 백준 12904 : A와 B
# LEVEL : Gold 4

import sys 
from collections import deque
input = sys.stdin.readline

def solution():
    S = input().rstrip()
    T = input().rstrip()
    s_length = len(S)

    while len(T) > s_length:
        if T[-1] == 'A':
            T = T[:-1]
        else:
            T = T[:-1][::-1]
        
    if T == S:
        print(1)
    else:
        print(0)


solution()
