from collections import deque

def solution(n, bans):
    bans.sort(key=lambda x: (len(x), x))
    bansQueue = deque(bans)
    
    while bansQueue:
        cur = bansQueue[0]
        target = get_string(n)
        if len(cur) < len(target) or (len(cur) == len(target) and cur <= target):
            bansQueue.popleft()
            n += 1
        else:
            break
            
    return get_string(n)

def get_string(n):
    sb = []
    while n > 0:
        remained = n % 26
        n //= 26
        if remained == 0:
            n -= 1
            sb.append('z')
        else:
            sb.append(chr(ord('a') + remained - 1))
    return ''.join(reversed(sb))