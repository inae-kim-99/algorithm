# https://programmers.co.kr/learn/courses/30/lessons/64065
# programmers 64065 : 2019 카카오 개발자 겨울 인턴십 - 튜플
# LEVEL 2

def solution(s):
    answer = []

    total_set = s[2:-2].split("},{")
    total_set = [sub_set.split(",") for sub_set in total_set]
    total_set.sort(key=len)

    for sub_set in total_set:
        for num in sub_set:
            if num not in answer:
                answer.append(num)

    answer = list(map(int, answer))
    return answer
