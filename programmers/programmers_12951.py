# https://programmers.co.kr/learn/courses/30/lessons/12951
# programmers 12951 : JadenCase 문자열 만들기
# LEVEL : 2

def solution(s):
    answer = ''
    is_first = True
    
    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            is_first = True
        else:
            if is_first:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            is_first = False
    
    return answer
        