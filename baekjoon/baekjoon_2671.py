# https://www.acmicpc.net/problem/2671
# 백준 2671 : 잠수함식별
# LEVEL : Gold 5

import sys
import re


def solution():
    sound = sys.stdin.readline().rstrip()

    pattern = re.compile('(100+1+|01)+')

    if pattern.fullmatch(sound):
        print("SUBMARINE")
    else:
        print("NOISE")


solution()
