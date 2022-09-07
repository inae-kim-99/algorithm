# https://www.acmicpc.net/problem/10816
# 백준 10816 : 숫자 카드 2
# LEVEL : Silver 4

import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right


def solution():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    find_nums = list(map(int, sys.stdin.readline().split()))

    d = defaultdict(int)
    for num in nums:
        d[num] += 1

    for num in find_nums:
        print(d[num], end=' ')

def solution_binary():
    N = int(sys.stdin.readline())
    nums = sorted(list(map(int, sys.stdin.readline().split())))

    M = int(sys.stdin.readline())
    find_nums = list(map(int, sys.stdin.readline().split()))

    for find_num in find_nums:
        left_index = bisect_left(nums, find_num)
        right_index = bisect_right(nums, find_num)
        print(right_index-left_index, end=' ')
    

solution_binary()
