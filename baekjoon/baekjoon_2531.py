# https://www.acmicpc.net/problem/2531
# baekjoon 2531 : 회전 초밥
# LEVEL : Silver 1

import sys
from collections import defaultdict


def solution():
    N, d, k, c = map(int, sys.stdin.readline().split())

    nums = [int(sys.stdin.readline()) for _ in range(N)]
    max_count = 0

    subset = defaultdict(int)
    subset[c] += 1
    count = 1

    for i in range(k): # 0 ~ k-1 초밥 먹기
        if not subset[nums[i]]:
            count += 1
        subset[nums[i]] += 1     
    
    for i in range(N-1): # i번째 초밥빼고 i+k번째 초밥 먹었을때의 경우 계산하기
        subset[nums[i]] -= 1
        if not subset[nums[i]]:
            count -= 1
        if not subset[nums[(i+k) % N]]:
            count += 1
        subset[nums[(i+k) % N]] += 1
        max_count = max(max_count, count)
    
    print(max_count)


solution()
