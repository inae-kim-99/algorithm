# https://programmers.co.kr/learn/courses/30/lessons/87946
# programmers 87946 : 위클리 챌린지 - 피로도
# LEVEL : 2

from collections import deque


def solution(k, dungeons):
    answer = -1
    length = len(dungeons)

    dq = deque([(k, [])])
    while dq:
        p, visited = dq.popleft()
        if len(visited) > answer:
            answer = len(visited)
        for i in range(length):
            if i not in visited and p >= dungeons[i][0]:
                dq.append((p-dungeons[i][1], visited + [i]))

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
