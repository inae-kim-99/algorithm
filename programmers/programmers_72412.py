# https://programmers.co.kr/learn/courses/30/lessons/72412
# programmers : 2021 KAKAO BLIND RECRUITMENT - 순위 검색
# LEVEL : 2
# 지원자 정보의 종류가 많지 않으므로,
# dictionary를 활용하여 모든 경우의 수에 해당 점수를 리스트로 추가하고
# query의 정보를 dictionary에서 찾아, 점수 리스트를 이분탐색 방법으로 확인한다.

from itertools import combinations


def solution(info, query):
    answer = []
    option = {}

    for applicant in info:
        applicant = applicant.split(' ')
        for i in range(5):
            for c in combinations(applicant[:-1], i):
                c = "".join(c)
                if option.get(c) is None:
                    option[c] = [int(applicant[-1])]
                else:
                    option[c].append(int(applicant[-1]))

    for value in option.values():
        value.sort()

    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q_option = "".join(q[:-1]).replace('and', '').replace('-', '')
        scores = option.get(q_option)
        if scores is None:
            answer.append(0)
        else:
            start, end = 0, len(scores)
            while start < end:
                mid = (start + end) // 2
                if scores[mid] >= q_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(scores)-start)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
