# https://www.acmicpc.net/problem/1920
# 백준 1920 : 수 찾기
# LEVEL : Silver 4
import sys


def solution():
    
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    find_nums = list(map(int, sys.stdin.readline().split()))

    nums.sort()

    def binary_search(target, start, end):
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return 0

    for i in range(M):
        print(binary_search(find_nums[i], 0, N))
    

solution()
