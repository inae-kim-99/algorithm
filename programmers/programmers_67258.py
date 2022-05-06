# https://programmers.co.kr/learn/courses/30/lessons/67258
# programmers 67258 : 2020 카카오 인턴십 - 보석 쇼핑
# LEVEL : 3

def solution(gems):
    answer = [0, len(gems)]
    types = set(gems)
    count = {}

    start = 0
    for end in range(len(gems)):
        count[gems[end]] = count.get(gems[end], 0) + 1

        if len(count) == len(types):
            while count[gems[start]] > 1:
                count[gems[start]] -= 1
                start += 1

            if end - start < answer[1] - answer[0]:
                answer[0], answer[1] = start+1, end+1

    return answer
