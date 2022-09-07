# https://www.acmicpc.net/problem/9375
# 백준 9375 : 패션왕 신해빈
# LEVEL : Silver 3

import sys
from collections import defaultdict

def solution():
    TC = int(sys.stdin.readline())

    for _ in range(TC):
        clothes = defaultdict(set)

        N = int(sys.stdin.readline())

        for _ in range(N):
            cname, ctype = sys.stdin.readline().rstrip().split()
            clothes[ctype].add(cname)
        
        answer = 1
        for names in clothes.values():
            answer *= (len(names)+1)
        
        print(answer - 1)

solution()




