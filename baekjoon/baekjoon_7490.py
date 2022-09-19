# https://www.acmicpc.net/problem/7490
# 백준 7490 : 0 만들기
# LEVEL : Gold 5

import sys


def solution():
    TC = int(sys.stdin.readline())

    for _ in range(TC):

        N = int(sys.stdin.readline())
        make("1", 2, N)
        print()
        

def make(expression, number, n):
    if number > n:
        if eval(expression.replace(' ', '')) == 0:
            print(expression)
        return
    
    make(expression+' '+str(number), number+1, n)
    make(expression+'+'+str(number), number+1, n)
    make(expression+'-'+str(number), number+1, n)


solution()