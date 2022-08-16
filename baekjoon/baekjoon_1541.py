# https://www.acmicpc.net/problem/1541
# 백준 1541 : 잃어버린 괄호
# LEVEL : Silver 2
import sys


def solution():
    calculation = sys.stdin.readline().rstrip().split('-')

    ans = sum(map(int, calculation[0].split('+')))
    for i in range(1, len(calculation)):
        ans -= sum(map(int, calculation[i].split('+')))

    print(ans)


solution()
