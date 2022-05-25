# https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3
# programmers 42884 : 단속카메라
# LEVEL : 3

def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[0], reverse=True)
    
    camera = 30001
    for route in routes:
        if camera > route[1]:
            answer += 1
            camera = route[0]
            
    return answer