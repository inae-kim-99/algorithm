# https://programmers.co.kr/learn/courses/30/lessons/70128
# programmers 70128 : 월간 코드 챌린지 시즌1 - 내적
# LEVEL1

def solution(a, b):
    return sum([x*y for x, y in zip(a, b)])
