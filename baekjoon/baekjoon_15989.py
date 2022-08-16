# https://www.acmicpc.net/problem/15989
# 백준 15989 : 1,2,3 더하기 4
# LEVEL : Silver 1
import sys

def solution():
    T = int(sys.stdin.readline().rstrip())
    
    for _ in range(T):
        N = int(sys.stdin.readline().rstrip())

        if N <= 3:
            print(N)
        else:
            for i in range(N//3+1):
                