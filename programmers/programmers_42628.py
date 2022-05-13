import heapq
# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3#
# programmers 42628 : 힙(heap) - 이중우선순위큐
# LEVEL : 3

def solution(operations):
    answer = []
    
    hq, rhq = [], []
    count = 0
    for op in operations:
        [command, number] = op.split(' ')
        if command == 'I':
            heapq.heappush(hq, int(number))
            heapq.heappush(rhq, -int(number))
            count += 1
        else:
            if len(hq) + len(rhq) > count:   
                if number == '1':
                    heapq.heappop(rhq)
                else:
                    heapq.heappop(hq)
                count -= 1
                if count == 0:
                    hq, rhq = [], []
                    
    if count > 0:   
        return [-rhq[0], hq[0]]
    else:
        return [0, 0]
    
    return answer