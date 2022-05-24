# https://programmers.co.kr/learn/courses/30/lessons/43238
# programmers 43238 : 이분탐색 - 입국심사
# LEVEL : 3

def solution(n, times):
    answer = 0

    left, right = 0, n * max(times)
    while left <= right:
        people = 0
        mid = (left + right) // 2

        for time in times:
            people += (mid // time)
            if people > n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
