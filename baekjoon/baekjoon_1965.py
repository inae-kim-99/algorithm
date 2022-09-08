# https://www.acmicpc.net/problem/1965
# 백준 1965 : 상자넣기
# LEVEL : Silver 2

import sys


def solution():
    N = int(sys.stdin.readline())
    boxes = list(map(int, sys.stdin.readline().split()))
    
    ans = []
    for box in boxes:
        if not ans:
            ans.append(box)
        else:
            for i in range(len(ans)):
                if box <= ans[i]:
                    ans[i] = box
                    break
            else:
                ans.append(box)

    print(len(ans))


solution()
