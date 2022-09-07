# https://www.acmicpc.net/problem/6603
# 백준 6603 : 로또
# LEVEL : Silver 2

import sys
from itertools import combinations
input = sys.stdin.readline


def solution():
    while True:
        nums = input().rstrip()
        if nums == "0":
            break
        
        nums = list(map(int, nums.split()))[1:]
        cases = list(combinations(nums, 6))

        for case in cases:
            for n in case:
                print(n, end=" ")
            print()
        print()
    

solution()


