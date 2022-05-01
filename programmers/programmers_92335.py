# https://programmers.co.kr/learn/courses/30/lessons/92335
# programmers 92335 : 2022 KAKAO BLIND RECRUITMENT - K진수에서 소수 개수 구하기
# LEVEL : 2

from math import sqrt


def solution(n, k):
    answer = 0

    n_base = ''
    while n > 0:
        n_base += str(n % k)
        n //= k
    n_base = n_base[::-1]+'0'

    start = 0
    for i in range(0, len(n_base)):
        if n_base[i] == '0':
            if start != i and is_prime(int(n_base[start:i])):
                answer += 1
            start = i+1

    return answer


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False

    return True
