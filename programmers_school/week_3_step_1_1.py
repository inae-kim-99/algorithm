from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K:
        if len(scoville) >= 2:
            new_scoville = heappop(scoville) + heappop(scoville) * 2
            heappush(new_scoville)
            answer += 1
        else:
            return -1
    
    return answer