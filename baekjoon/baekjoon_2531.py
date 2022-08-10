# https://www.acmicpc.net/problem/2531
# baekjoon 2531 : 회전 초밥
# LEVEL : Silver 1

import sys
from collections import defaultdict

[N, d, k, c] = list(map(int, sys.stdin.readline().split()))

belts = []
eat, count = defaultdict(int), 0
max_type = 0

for _ in range(N):
    belts.append(int(sys.stdin.readline()))

for idx in range(k): # condition 개수 만큼 먹는다.
    if eat[belts[idx]] == 0:
        count += 1
    eat[belts[idx]] += 1

for left in range(N+k): # 최댓값 계산 후, idx + 1부터 condition개를 연속으로 먹은 경우의 초밥 종류 수를 계산한다.
    if eat[c] == 0:
        max_type = max(count + 1, max_type)
    else:
        max_type = max(count, max_type)
    
    eat[belts[left % N]] -= 1
    if eat[belts[left % N]] == 0:
        count -= 1
    
    eat[belts[(left+k) % N]] += 1
    if eat[belts[(left+k) % N]] == 1:
        count += 1

print(max_type)
