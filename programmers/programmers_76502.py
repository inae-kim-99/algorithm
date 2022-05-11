# https://programmers.co.kr/learn/courses/30/lessons/76502
# programmers 76502 : 월간 코드 챌린지 시즌2 - 괄호 회전하기
# LEVEL : 2

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if i:
            s = s[1:] + s[0]
        stack = []
        for bracket in s:
            if not stack or bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if (bracket == ')' and stack[-1] == '(') or \
                (bracket == '}' and stack[-1] == '{') or \
                (bracket == ']' and stack[-1] == '['):
                    stack.pop()
        if not stack:
            answer += 1
            
    return answer