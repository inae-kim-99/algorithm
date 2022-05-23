# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3#
# programmers 43164 : 여행 경로
# LEVEL : 3

from collections import defaultdict


def solution(tickets):
    answer = []

    route = defaultdict(list)
    for ticket in tickets:
        route[ticket[0]].append(ticket[1])
    for values in route.values():
        values.sort(reverse=True)

    stack = ["ICN"]
    while stack:
        if not route[stack[-1]]:
            answer.append(stack.pop())
        else:
            stack.append(route[stack[-1]].pop())

    answer.reverse()
    return answer
