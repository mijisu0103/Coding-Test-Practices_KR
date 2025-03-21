def solution(stones, k):
    answer = 0
    
    left, right, ct = 1, max(stones), 0
    
    while left <= right:
        ct = 0
        mid = (left + right) // 2
        
        for stone in stones:
            if (stone - mid) <= 0:
                ct += 1
            else:
                ct = 0
            if ct >= k:
                break
        if ct < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer
