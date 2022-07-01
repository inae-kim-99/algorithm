# https: // programmers.co.kr/learn/courses/30/lessons/72414?language = python3
# programmers 72414 : 2021 KAKAO BLIND RECRUITMENT - 광고 삽입

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    play_time, adv_time = str_to_sec(play_time), str_to_sec(adv_time)
    time = [0] * (play_time+1)

    for log in logs:
        [start_time, end_time] = log.split('-')
        start_time = str_to_sec(start_time)
        end_time = str_to_sec(end_time)
        time[start_time] += 1
        time[end_time] -= 1

    for i in range(1, len(time)):
        time[i] += time[i-1]
    for i in range(1, len(time)):
        time[i] += time[i-1]

    max_time, max_index = time[adv_time], 0
    for i in range(adv_time, play_time):
        total_time = time[i] - time[i-adv_time]
        if total_time > max_time:
            max_time = total_time
            max_index = i - adv_time + 1

    return sec_to_str(max_index)


def str_to_sec(time):
    [hour, minute, second] = list(map(int, time.split(':')))
    return hour * 3600 + minute * 60 + second


def sec_to_str(sec):
    hour = sec // 3600
    minute = (sec // 60) % 60
    second = sec % 60
    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
