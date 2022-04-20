# 1주차 Step1-3. 문제 먼저 직접 풀어보기 "가장 큰 수"

from functools import cmp_to_key


def solution(numbers):
    numbers = sorted([str(n) for n in numbers], key=cmp_to_key(compare))
    return int("".join(numbers)

def compare(a, b):
    if int(a+b) > int(b+a):
        return -1
    else:
        return 1

print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))
print(solution([0, 10, 6]))
print(solution([0, 0, 0, 0]))
