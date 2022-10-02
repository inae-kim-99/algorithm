# https://www.acmicpc.net/problem/1253
# 백준 1253 : 좋다
# LEVEL : Gold 4

import sys
from collections import defaultdict
input = sys.stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    count = 0
    
    for i in range(N):
        arr = A[:i] + A[i+1:]
        target = A[i]

        start = 0
        end = len(arr)-1
        while start < end:
            num = arr[start] + arr[end]

            if num == target:
                count += 1
                break

            if num > target:
                end -= 1
            else:
                start += 1
    
    print(count)
        

solution()