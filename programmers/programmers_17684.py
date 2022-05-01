# https://programmers.co.kr/learn/courses/30/lessons/17684
# programmers 17684 : 2018 KAKAO BLIND RECRUITMENT - [3차] 압축
# LEVEL : 2

def solution(msg):
    answer = []
    dict = {chr(e + 64): e for e in range(1, 27)}

    msg += 'x'
    start, new_index = 0, 27
    for i in range(len(msg)):
        if dict.get(msg[start:i+1]) == None:
            answer.append(dict[msg[start:i]])
            dict[msg[ start:i+1]] = new_index
            new_index += 1
            start = i

    return answer