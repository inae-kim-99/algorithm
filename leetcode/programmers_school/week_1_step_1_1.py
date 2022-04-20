# 1주차 Step1-1. 문제 먼저 직접 풀어보기 "완주하지 못한 선수"

# solution1
def solution(participant, completion):
    for p, c in zip(sorted(participant), sorted(completion)+[""]):
        if p != c:
            return p


# solution2
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
