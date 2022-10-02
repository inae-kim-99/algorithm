# https://www.acmicpc.net/problem/11509
# 백준 11509 : 풍선 맞추기
# LEVEL : Gold 5

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    heights = list(map(int, input().split()))

    arrows = [0] * (1000001)

    for h in heights:
        if arrows[h] == 0:
            arrows[h-1] += 1
        else:
            arrows[h] -= 1
            arrows[h-1] += 1
    
    print(sum(arrows))

        
solution()