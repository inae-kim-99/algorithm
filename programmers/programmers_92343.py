# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# programmers 92343 : 2022 KAKAO BLIND RECRUITMENT - 양과 늑대
# LEVEL : 3

def solution(info, edges):
    answer = []

    visited = [False] * len(info)
    visited[0] = 1

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            is_wolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(sheep+(is_wolf == 0), wolf+(is_wolf == 1))
                visited[child] = False

    dfs(1, 0)
    return max(answer)
