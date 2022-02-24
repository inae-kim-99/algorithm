# https://programmers.co.kr/learn/courses/30/lessons/12973
# programmers 12973 : 2017 팁스타운 - 짝지어 제거하기
# LEVEL 2

def solution(s):
    stack = [s[0], ]
    for i in range(1, len(s)):
        if len(stack) > 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack) > 0:
        return 0
    else:
        return 1
