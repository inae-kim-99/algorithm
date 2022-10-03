# https://www.acmicpc.net/problem/21921
# 백준 21921 : 블로그
# LEVEL : Silver 3

import sys
input = sys.stdin.readline

def solution():
    N, X = map(int, input().split())
    nums = list(map(int, input().split()))

    total = sum(nums[:X])
    
    answer = total
    same = 1

    for i in range(N-X):
        total -= nums[i]
        total += nums[i+X]
        if total > answer:
            answer = total
            same = 1
        elif total == answer:
            same += 1

    if answer == 0:
        print("SAD")
    else:
        print(answer)
        print(same)
    

solution()