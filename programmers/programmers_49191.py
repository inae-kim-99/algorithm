# https://programmers.co.kr/learn/courses/30/lessons/49191
# programmers 49191 : 그래프 - 순위
# LEVEL : 3

from collections import defaultdict


def solution(n, results):
    answer = 0

    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for result in results:
        win_graph[result[0]].add(result[1])
        lose_graph[result[1]].add(result[0])

    for player in range(1, n+1):
        for win_player in lose_graph[player]:
            win_graph[win_player].update(win_graph[player])
        for lose_player in win_graph[player]:
            lose_graph[lose_player].update(lose_graph[player])

    for player in range(1, n+1):
        if len(win_graph[player]) + len(lose_graph[player]) == n-1:
            answer += 1

    return answer
