# https://programmers.co.kr/learn/courses/30/lessons/86971
# programmers 86971 : 위클리 챌린지 - 전력망을 둘로 나누기
# LEVEL : 2

from collections import deque


def solution(n, wires):
    def counting(root, cut_node):
        dq, visited = deque([root]), [False for _ in range(n+1)]
        visited[root] = True
        while dq:
            node = dq.popleft()
            for i in range(1, n+1):
                if not visited[i] and i != cut_node and tree[node][i]:
                    visited[i] = True
                    dq.append(i)
        return visited.count(True)

    answer = 100

    tree = [[False for _ in range(n+1)] for _ in range(n+1)]
    for wire in wires:
        tree[wire[0]][wire[1]] = True
        tree[wire[1]][wire[0]] = True

    for wire in wires:
        answer = min(answer, abs(
            counting(wire[0], wire[1])-counting(wire[1], wire[0])))

    return answer
