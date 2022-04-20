# 1주차 Step1-2. 문제 먼저 직접 풀어보기 "체육복"

def solution(n, lost, reserve):
    students = [1] * n
    zero = 0

    for l in lost:
        students[l-1] -= 1
    for r in reserve:
        students[r-1] += 1

    for i in range(n):
        if students[i] == 0:
            if i != 0 and students[i-1] == 2:
                students[i] += 1
                students[i-1] -= 1
            elif i != n-1 and students[i+1] == 2:
                students[i] += 1
                students[i+1] -= 1
            else:
                zero += 1

    return n - zero
