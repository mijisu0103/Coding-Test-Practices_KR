from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    count = len(queue1) + len(queue2) + 2
    answer = 0
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while sum1 != sum2:        
        if count > 0:
            if sum1 < sum2:
                i = queue2.popleft()
                queue1.append(i)
                sum2 -= i
                sum1 += i
                count -= 1
                answer += 1

            elif sum1 > sum2:
                i = queue1.popleft()
                queue2.append(i)
                sum1 -= i
                sum2 += i
                count -= 1
                answer += 1
        
        else:
            return -1
            
    return answer