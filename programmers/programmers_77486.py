# https://programmers.co.kr/learn/courses/30/lessons/77486
# programmers 77486 : 2021-Dev-Matching: 웹 백엔드 개발 - 다단계 칫솔 판매
# LEVEL : 3

def solution(enroll, referral, seller, amount):
    answer = []

    profit, recommender = {}, {}

    for e, r in zip(enroll, referral):
        recommender[e] = r

    for s, a in zip(seller, amount):
        profit[s] = profit.get(s, 0) + int(a * 90)
        parent, remain = recommender[s], int(a * 10)
        while parent != '-':
            if remain >= 10:
                profit[parent] = profit.get(parent, 0) + (remain - remain//10)
                parent, remain = recommender[parent], remain//10
            else:
                profit[parent] = profit.get(parent, 0) + remain
                break

    for e in enroll:
        answer.append(profit.get(e, 0))

    return answer
