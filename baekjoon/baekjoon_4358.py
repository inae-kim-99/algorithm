# https://www.acmicpc.net/problem/4358
# 백준 4358 : 생태학
# LEVEL : Silver 2

import sys
from collections import defaultdict


def solution():
    trees = defaultdict(int)
    tree_num = 0

    while True:
        name = sys.stdin.readline().rstrip()
        if name == "":
            break
        trees[name] += 1
        tree_num += 1

    names = sorted(trees.keys())

    for name in names:
        # print(f"{name} {round(trees[name]*100/tree_num, 4)}")
        print('%s %.4f' %(name, (trees[name]/tree_num*100)))


solution()
# print(round(2.255, 2))
# print(round(2.265, 2))