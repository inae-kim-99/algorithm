# https://www.acmicpc.net/problem/4948
# 백준 4948 : 베르트랑 공준
# LEVEL : Silver 3

import sys
from math import sqrt


def solution():
    MAX_INDEX = 123456 * 2

    primes = [0] * (MAX_INDEX + 1)
    primes[1] = 1

    for i in range(2, MAX_INDEX + 1):
        primes[i] += primes[i-1]
        if is_prime(i):
            primes[i] += 1

    while True:
        N = int(sys.stdin.readline())
        if N == 0:
            return
        print(primes[N*2] - primes[N])


def is_prime(n):
    if n <= 2:
        return 1

    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True


solution()
