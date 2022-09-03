# https://school.programmers.co.kr/learn/courses/30/lessons/67256
# programmers 67275 : 2020 카카오 인턴십 - 키패드 누르기
# LEVEL : 1

def get_loc(number):
    if number == "*":
        return [3, 0]
    elif number == "#":
        return [3, 2]
    elif number == 0:
        return [3, 1]
    else:
        return [(number-1)//3, (number-1) % 3]


def solution(numbers, hand):
    answer = ''

    use = {1: 'L', 4: 'L', 7: 'L', 3: 'R', 6: 'R',
           9: 'R', 2: 'M', 5: 'M', 8: 'M', 0: 'M'}
    hand_use = {"left": 'L', "right": "R"}

    left, right = "*", "#"

    for number in numbers:
        if use[number] == "M":
            l_loc, r_loc, n_loc = get_loc(
                left), get_loc(right), get_loc(number)
            l_dist, r_dist = abs(
                l_loc[0]-n_loc[0])+abs(l_loc[1]-n_loc[1]), abs(r_loc[0]-n_loc[0])+abs(r_loc[1]-n_loc[1])

            if l_dist == r_dist:
                answer += hand_use[hand]
                if hand == "left":
                    left = number
                else:
                    right = number
            elif l_dist < r_dist:
                answer += 'L'
                left = number
            else:
                answer += 'R'
                right = number
        else:
            answer += use[number]
            if use[number] == "L":
                left = number
            else:
                right = number

    return answer


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
