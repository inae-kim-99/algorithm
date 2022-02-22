# https://programmers.co.kr/learn/courses/30/lessons/76501
# programmers 76501 : 월간 코드 챌린지 시즌2 - 음양 더하기
# LEVEL 1

def solution(absolutes, signs):
    answer = 0

    for number, sign in zip(absolutes, signs):
        if sign:
            answer += number
        else:
            answer -= number

    return answer
