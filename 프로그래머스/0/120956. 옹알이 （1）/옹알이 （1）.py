def solution(babbling):
    
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        for c in can:
            if c in b:
                b = b.replace(c, "*")
        if len(b) == b.count("*"):
            answer += 1
            
    return answer