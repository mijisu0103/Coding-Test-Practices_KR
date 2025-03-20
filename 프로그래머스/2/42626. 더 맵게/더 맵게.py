import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville) > 1:
        min_sco = heapq.heappop(scoville)
        if min_sco >= K:
            return answer
        else:
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, min_sco + second*2)
            answer += 1
    if scoville[0] >= K:
        return answer
    return -1
        