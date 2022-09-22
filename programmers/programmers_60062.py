# https://school.programmers.co.kr/learn/courses/30/lessons/60062
# programmers 60062 : 외벽 점검
# LEVEL : 3

from itertools import permutations


def solution(n, weak, dist):
    w_length = len(weak)
    for i in range(w_length):
        weak.append(n + weak[i])

    d_length = len(dist)

    answer = d_length + 1

    for i in range(w_length):
        for d in list(permutations(dist, d_length)):
            d_idx, d_dist = 0, d[0]
            w_idx = i

            while w_idx < i + w_length and d_idx < d_length:  # weak와 friend를 다 확인할 때까지
                if w_idx == i+w_length-1:
                    break
                if d_dist < weak[w_idx+1] - weak[w_idx]:  # f_idx 친구가 갈 수 없을 때
                    w_idx += 1
                    d_idx += 1
                    if d_idx < d_length:
                        d_dist = d[d_idx]
                else:  # f_idx 친구가 갈 수 있으면 보냄
                    d_dist -= (weak[w_idx+1] - weak[w_idx])
                    w_idx += 1

            if d_idx < d_length:
                answer = min(answer, d_idx+1)

    if answer == d_length + 1:
        answer = -1

    return answer
