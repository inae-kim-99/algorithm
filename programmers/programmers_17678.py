# https://programmers.co.kr/learn/courses/30/lessons/17678
# programmers 17678 : 2018 KAKAO BLIND RECRUITMENT - [1차] 셔틀 버스
# LEVEL : 3

def solution(n, t, m, timetable):
    answer = 0
    timetable = [int(t[:2])*60+int(t[3:]) for t in timetable]
    timetable.sort()

    crew_i = 0
    for i in range(n):
        time = 540 + i*t
        crews = []
        while crew_i < len(timetable) and len(crews) < m and timetable[crew_i] <= time:
            crews.append(timetable[crew_i])
            crew_i += 1
        if len(crews) < m:
            answer = time
        else:
            answer = max(crews)-1

    return str(answer//60).zfill(2) + ":" + str(answer % 60).zfill(2)
