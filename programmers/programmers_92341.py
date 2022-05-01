# https://programmers.co.kr/learn/courses/30/lessons/92341
# programmers 92341 : 2022 KAKAO BLIND RECRUITMENT - 주차 요금 계산
# LEVEL : 2

def solution(fees, records):
    answer = []
    inout, time = {}, {}

    # 누적 시간 저장만
    for record in records:
        record = record.split(' ')
        if record[2] == 'IN':
            inout[record[1]] = record[0]
        else:
            before = time.get(record[1], 0)
            time[record[1]] = before + calc_time(inout[record[1]], record[0])
            del inout[record[1]]

    # 남은 차들
    for car, t in inout.items():
        before = time.get(car, 0)
        time[car] = before + calc_time(t, '23:59')
        print(time[car])

    # 요금 계산
    time = list(time.items())
    time.sort(key=lambda x: x[0])
    for car, t in time:
        fee, t = fees[1], t-fees[0]
        if t > 0:
            fee += (t//fees[2]) * fees[3] + (0 if t %
                                             fees[2] == 0 else fees[3])
        answer.append(fee)

    return answer


def calc_time(t1, t2):
    return int(t2[:2])*60 + int(t2[3:]) - int(t1[:2])*60 - int(t1[3:])


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
           "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
