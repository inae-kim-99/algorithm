# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
# programmers 42839 : 소수 찾기
# LEVEL : 2

from math import sqrt
from itertools import permutations


def solution(numbers):
    numbers = [n for n in numbers]
    answer = set()

    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            if is_prime(num):
                answer.add(num)

    return len(answer)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
