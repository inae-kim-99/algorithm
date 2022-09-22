# https://school.programmers.co.kr/learn/courses/30/lessons/92344
# programmers 92344 : 파괴되지 않은 건물
# LEVEL : 3

def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    temp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(len(skill)):
        [type, r1, c1, r2, c2, degree] = skill[i]

        if type == 1:
            degree = -degree

        temp[r1][c1] += degree
        temp[r2 + 1][c2 + 1] += degree
        temp[r1][c2 + 1] -= degree
        temp[r2 + 1][c1] -= degree

    # 열 기준 누적합
    for i in range(N):
        for j in range(M):
            temp[i][j+1] += temp[i][j]

    # 행 기준 누적합
    for j in range(M):
        for i in range(N):
            temp[i+1][j] += temp[i][j]

    for i in range(N):
        for j in range(M):
            if board[i][j] + temp[i][j] > 0:
                answer += 1

    return answer
