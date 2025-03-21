def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    # 2
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
            
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer [-1] == '.' else answer
    
    # 5
    answer = 'a' if answer == '' else answer
    
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 7
    if len(answer) <= 3:
        answer = answer + answer[-1] * (3-len(answer)) 
    
    return answer