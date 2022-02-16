# https://programmers.co.kr/learn/courses/30/lessons/72410
# programmers 72410 : 2021 KAKAO BLIND RECROUITMENT 신규 아이디 추천
# LEVEL 1

import re


def solution(new_id):
    answer = new_id.lower()

    answer = "".join(re.findall("[a-z0-9-_.]", answer))

    while ".." in answer:
        answer = answer.replace("..", ".")

    answer = answer.strip(".")

    if len(answer) == 0:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip(".")

    id_length = len(answer)
    if id_length <= 2:
        for i in range(3-id_length):
            answer += answer[id_length-1]

    return answer
