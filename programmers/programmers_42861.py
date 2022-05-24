# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3
# programmers 42861 : 섬 연결하기
# LEVEL : 3

from collections import deque


def solution(n, costs):
    answer = 0

    weight = [[-1 for _ in range(n)] for _ in range(n)]
    for cost in costs:
        weight[cost[0]][cost[1]] = cost[2]
        weight[cost[1]][cost[0]] = cost[2]

    visited = [0]
    while len(visited) < n:
        min_weight, new_node = 1e9, -1
        for node in visited:
            for neighbor in range(n):
                if neighbor not in visited and weight[node][neighbor] != -1:
                    if weight[node][neighbor] < min_weight:
                        new_node = neighbor
                        min_weight = weight[node][neighbor]

        visited.append(new_node)
        answer += min_weight

    return answer
