# https://www.acmicpc.net/problem/2961
# 백준 2961 : 도영이가 만든 맛있는 음식
# LEVEL : Silver 2
import sys


def solution_bitmask():
    N = int(sys.stdin.readline())
    ingredients = [list(map(int, sys.stdin.readline().split()))
                   for _ in range(N)]
    answer = sys.maxsize

    for i in range(1, 1 << N):
        sour, bitter = 1, 0
        for j in range(N):
            if i & (1 << j):
                sour *= ingredients[j][0]
                bitter += ingredients[j][1]
        answer = min(answer, abs(sour-bitter))

    print(answer)


def solution():
    N = int(sys.stdin.readline())
    ingredients = [list(map(int, sys.stdin.readline().split()))
                   for _ in range(N)]
    answer = []

    def dfs(sour, bitter, i):
        if i == N:
            if bitter != 0:
                answer.append(abs(sour-bitter))
            return

        dfs(sour*ingredients[i][0], bitter+ingredients[i][1], i+1)
        dfs(sour, bitter, i+1)

    dfs(1, 0, 0)

    print(min(answer))


solution_bitmask()
