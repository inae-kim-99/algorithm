# https://programmers.co.kr/learn/courses/30/lessons/81302
# programmers 81302 : 2021 카카오 채용연계형 인턴십 - 거리두기 확인하기
# LEVEL : 2

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = {'P': 1, 'O': 2}


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer


def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'X':
                find = 0
                for x, y in zip(dx, dy):
                    if is_range(i+y, j+x) and place[i+y][j+x] == 'P':
                        find += 1
                if find >= count[place[i][j]]:
                    return 0
    return 1


def is_range(y, x):
    return (y >= 0 and y < 5 and x >= 0 and x < 5)
