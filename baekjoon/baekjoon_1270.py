# https://www.acmicpc.net/problem/1270
# 백준 1270 : 전쟁 - 땅따먹기
# LEVEL : Silver 3

import sys
from collections import defaultdict

def solution():
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        half_soldier, nums = row[0]//2, row[1:]
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        state = "SYJKGW"
        for key, value in count.items():
            if value > half_soldier:
                state = key
                break

        print(state)

solution()