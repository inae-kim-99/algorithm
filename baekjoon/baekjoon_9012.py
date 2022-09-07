# https://www.acmicpc.net/problem/9012
# 백준 9012 : 괄호
# LEVEL : Silver

import sys

def solution():
    TC = int(sys.stdin.readline())

    for _ in range(TC):
        parenthesis = sys.stdin.readline().rstrip()
        
        check = 0
        for p in parenthesis:
            if p == '(':
                check += 1
            else:
                if check == 0:
                    print("NO")
                    break
                check -= 1
        else:
            if check == 0:
                print("YES")
            else:
                print("NO")
    
solution()