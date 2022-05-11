# https://programmers.co.kr/learn/courses/30/lessons/12913
# programmers 12913 : 땅따먹기
# LEVEL : 2

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            before_max = 0
            for k in range(4):
                if k != j and land[i-1][k] > before_max:
                    before_max = land[i-1][k]
            land[i][j] += before_max

    return max(land[-1])
