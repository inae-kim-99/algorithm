# https://programmers.co.kr/learn/courses/30/lessons/77884
# programmers 77884 : 월간 코드 챌린지 시즌2 - 약수의 개수와 덧셈
# LEVEL 1

import math


def solution(left, right):
    answer = 0

    for i in range(left, right+1):
        sqrt = math.sqrt(i)
        if int(sqrt) == sqrt:
            answer -= i
        else:
            answer += i

    return answer
