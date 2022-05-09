# https://programmers.co.kr/learn/courses/30/lessons/12905
# programmers 12905 : 가장 큰 정사각형 찾기
# LEVEL : 2

def solution(board):
    answer = 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            answer = max(answer, board[i][j])
    
    return answer*answer