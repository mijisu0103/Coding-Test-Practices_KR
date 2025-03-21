def solution(seoul):
    answer = ''
    
    for i in seoul:
        if i == "Kim":
            answer = seoul.index(i)
    
    return f"김서방은 {answer}에 있다"