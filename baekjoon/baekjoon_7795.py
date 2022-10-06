# https://www.acmicpc.net/problem/7795
# 백준 7795 : 먹을 것인가 먹힐 것인가
# LEVEL : Silver 3

import sys
input = sys.stdin.readline


def solution():
    TC = int(input())

    for _ in range(TC):

        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        B.sort()

        count = 0

        for target in A:
            if target <= B[0]:
                continue

            start = 0
            end = M-1

            max_index = -1
            
            while start <= end:
                mid = (start + end) // 2

                if B[mid] < target:
                    start = mid + 1
                    max_index = max(max_index, mid)
                else:
                    end = mid - 1

            count += (max_index + 1)
        
        print(count)

solution()

            
