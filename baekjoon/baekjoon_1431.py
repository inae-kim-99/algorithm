# https://www.acmicpc.net/problem/1431
# 백준 1431 : 시리얼 번호
# LEVEL : Silver 3

import sys
import re


def solution():
    N = int(sys.stdin.readline())
    guitars = [sys.stdin.readline().rstrip() for _ in range(N)]

    serial_lengths = {}  # serial 길이
    serial_sums = {}  # 숫자의 합
    for guitar in guitars:
        serial_lengths[guitar] = len(guitar)
        serial_sums[guitar] = sum(map(int, re.findall(r'\d', guitar)))

    def swap(i, j):
        guitars[i], guitars[j] = guitars[j], guitars[i]

    for i in range(N):
        for j in range(N-i-1):
            g1, g2 = guitars[j], guitars[j+1]
            if serial_lengths[g1] > serial_lengths[g2]:
                swap(j, j+1)
            elif serial_lengths[g1] == serial_lengths[g2]:
                if serial_sums[g1] > serial_sums[g2] or \
                        serial_sums[g1] == serial_sums[g2] and guitars[j] > guitars[j+1]:
                    swap(j, j+1)

    for guitar in guitars:
        print(guitar)


solution()
