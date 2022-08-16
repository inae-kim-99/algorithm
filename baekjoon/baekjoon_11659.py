# https://www.acmicpc.net/problem/11659
# 백준 11659 : 구간 합 구하기 4
# LEVEL : Silver 3
import sys

def solution():
    [N, M] = list(map(int, sys.stdin.readline().rstrip().split()))
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    part_sum = [0] + nums.copy()
    
    for i in range(1, N+1):
        part_sum[i] += part_sum[i-1]
    
    for _ in range(M):
        [start, end] = list(map(int, sys.stdin.readline().rstrip().split()))
        print(part_sum[end] - part_sum[start-1])

solution()