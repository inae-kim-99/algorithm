# https://school.programmers.co.kr/learn/courses/30/lessons/72413
# programmers 72413 : 합승 택시 요금
# LEVEL : 3


def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    INF = float('inf')

    graph = [[INF for _ in range(n)] for _ in range(n)]
    for start, end, fare in fares:
        graph[start-1][end-1] = fare
        graph[end-1][start-1] = fare

    for i in range(n):
        graph[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = INF

    for k in range(n):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])
        print(answer, k)

    return answer
