# https://www.acmicpc.net/problem/2504
# 백준 2504 : 괄호의 값
# LEVEL : Silver 1

import sys
input = sys.stdin.readline

def solution():
    arr = input().rstrip()

    result = 0
    temp = 1
    stack = []

    for i in range(len(arr)):
        if arr[i] == '(':
            temp *= 2
            stack.append(arr[i])
        elif arr[i] == '[':
            temp *= 3
            stack.append(arr[i])
        elif arr[i] == ')':
            if stack and stack[-1] == '(':
                if arr[i-1] == '(':
                    result += temp
                temp //= 2
                stack.pop()
            else:
                result = 0
                break
        else:
            if stack and stack[-1] == '[':
                if arr[i-1] == '[':
                    result += temp
                temp //= 3
                stack.pop()
            else:
                result = 0
                break
        
    if stack:
        result = 0
        
    print(result)
        

solution()
