# https://programmers.co.kr/learn/courses/30/lessons/17676
# programmers 17676 : 2018 KAKAO BLIND RECRUITMENT - [1차] 추석 트래픽
# LEVEL : 3

def solution(lines):
    answer = 1
    timeline = []

    for log in lines:
        log = log.split(' ')
        end = (int(log[1][:2]) * 3600 +
               int(log[1][3:5]) * 60 + float(log[1][6:]))*1000
        start = end - float(log[2][:-1])*1000 + 1
        timeline.append((int(start), int(end)))

    timeline.sort(key=lambda x: x[0])

    for i in range(1, len(timeline)):
        count = 1
        for j in range(i):
            if timeline[j][1]+999 >= timeline[i][0]:
                count += 1
        answer = max(answer, count)

    return answer
