# https://www.acmicpc.net/problem/2512
# 백준 2512 : 예산
# LEVEL : Silver 3
import sys


def solution():
    N = int(sys.stdin.readline())
    requests = list(map(int, sys.stdin.readline().split()))
    budget = int(sys.stdin.readline())

    requests.sort()  # 예산 요청을 오름차순으로 정렬

    if sum(requests) <= budget:  # 모든 요청이 배정될 수 있는 경우
        print(requests[-1])  # 최댓값 출력 (정렬한 상태이기 때문에 [-1])
    else:  # 모든 요청이 배정될 수 없는 경우
        for i in range(N):
            mean = budget//(N-i)  # i번째 요청을 포함하여 평균적으로 줄 수 있는 예산
            if requests[i] <= mean:
                budget -= requests[i]
            else:
                print(mean)
                break


solution()
