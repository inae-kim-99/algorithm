# https://programmers.co.kr/learn/courses/30/lessons/17687
# programmers 17687 : 2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임
# LEVEL : 2

def solution(n, t, m, p):
    answer = ""

    order = ""
    idx, length = 0, (p-1)+t*m
    while len(order) < length:
        order += convert(idx, n)
        idx += 1

    for i in range(t):
        answer += order[p-1+m*i]

    return answer


def convert(n, x):
    number = ['0', '1', '2', '3', '4', '5', '6',
              '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    converted = ""
    while n > 0:
        converted += number[n % x]
        n //= x
    return converted[::-1] if converted else "0"
