# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
# programmers 12911 : 다음 큰 숫자
# LEVEL : 2

# 지난 풀이. 통과하지만 코드가 더러움 ..
# def solution(n):
#     answer = ''
#     n = bin(n)

#     count_one = 0
#     for i in range(len(n)-1, 1, -1):
#         if n[i] == '1':
#             count_one += 1
#         if n[i] == '0' and count_one > 0:
#             if count_one == 1:
#                 return int(n[:i] + '1' + '0'*(len(n)-i-1), 2)
#             else:
#                 return int(n[:i] + '10' + ('1'*(count_one-1)).zfill(len(n)-i-2), 2)

#     if count_one == len(n)-2:
#         return int('0b10'+('1'*(count_one-1)).zfill(count_one-1), 2)
#     else:
#         return int('0b10'+('1'*(count_one-1)).zfill(len(n)-count_one-1), 2)


def solution(n):
    count = bin(n).count('1')

    while bin(n+1).count('1') != count:
        n += 1

    return n+1
