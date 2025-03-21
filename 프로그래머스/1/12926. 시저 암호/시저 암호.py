def solution(s, n):
    answer = ''
    
    for ch in s:
        if ch.isupper():
            answer += chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        elif ch.islower():
            answer += chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += ch 
    
    return answer
