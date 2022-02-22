# https: // programmers.co.kr/learn/courses/30/lessons/12977
# programmers 12977 : Summer/Winter Coding(~2018) - 소수 만들기
# LEVEL 1

def solution(nums):
    answer = 0

    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer += 1

    return answer


def is_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True
