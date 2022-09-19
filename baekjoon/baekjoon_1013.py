# https://www.acmicpc.net/problem/1013
# 백준 1013 : Contact
# LEVEL : Gold 5

import sys
import re

def solution_fullmatch():
    T = int(sys.stdin.readline())

    for _ in range(T):
        pattern = sys.stdin.readline().rstrip()

        p = re.compile('(100+1+|01)+')
        result = p.fullmatch(pattern)

        if result:
            print("YES")
        else:
            print("NO")

def solution():
    T = int(sys.stdin.readline())

    for _ in range(T):
        pattern = sys.stdin.readline().rstrip()
        if match(pattern):
            print("YES")
        else:
            print("NO")


def match(pattern):
    if len(pattern) == 0:
        return True

    first_match = re.compile("100+").match(p)

    if first_match:
        index = first_match.end()
        while index < len(pattern) and pattern[index] == '1':
            if match(pattern[index+1:]):
                return True
            index += 1

    second_match = re.compile("01").match(pattern)

    if second_match:
        index = second_match.end()
        if match(pattern[index:]):
            return True

    return False


solution()
