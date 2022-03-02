# https://programmers.co.kr/learn/courses/30/lessons/68935
# programmers 68935 : 월간 코드 챌린지 시즌1 - 3진법 뒤집기
# LEVEL 1

def solution(n):
    number = ""

    while(n > 0):
        number += str(n % 3)
        n //= 3

    return int(number, 3)
