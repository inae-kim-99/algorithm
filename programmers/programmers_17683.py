# https://programmers.co.kr/learn/courses/30/lessons/17683
# programmers 17683 : 2018 KAKAO BLIND RECRUITMENT - [3차]방금그곡
# LEVEL : 2

def solution(m, musicinfos):
    m = replace(m)
    answer = [0, '(None)']

    for info in musicinfos:
        info = info.split(',')
        info[3] = replace(info[3])

        time = (int(info[1][:2]) * 60 + int(info[1][3:])) - \
            (int(info[0][:2]) * 60 + int(info[0][3:]))
        title = info[2]
        melody = info[3]*(time//len(info[3])) + \
            info[3][:(time % len(info[3]))]
        print(melody)

        if m in melody and time > answer[0]:
            answer = [time, title]

    return answer[-1]

def replace(str):
    return str.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

print(solution(m, musicinfos))
