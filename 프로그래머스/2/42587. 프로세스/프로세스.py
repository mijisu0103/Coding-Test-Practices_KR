from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    names = deque()
    
    for i in range(len(queue)):
        names.append(chr(ord('A')+i))
    alp = names[location]
    
    while alp in names:
        back = False
        x = queue.popleft()
        y = names.popleft()
        
        for q in queue:
            if x < q:
                queue.append(x)
                names.append(y)
                back = True
                break
        if back == False:
                answer += 1
    
    return answer