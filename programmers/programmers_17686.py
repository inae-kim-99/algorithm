# https://programmers.co.kr/learn/courses/30/lessons/17686
# programmers 17686 : 2018 KAKAO BLIND RECRUITMENT - [3차]파일명 정렬
# LEVEL : 2

import re


def solution(files):
    answer = []

    for file in files:
        head, number, tail = "", "", ""
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                for j in range(i+1, len(file)):
                    if not file[j].isdigit():
                        number = file[i:j]
                        tail = file[j:]
                        break
                break
        answer.append((head, number, tail))

    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(a) for a in answer]
