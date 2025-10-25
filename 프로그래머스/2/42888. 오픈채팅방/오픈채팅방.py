def solution(record):
    
    answer = []
    name_history = {}
    
    for rec in record:
        rec_chunk = rec.split()
        if len(rec_chunk) == 3:
            name_history[rec_chunk[1]] = rec_chunk[2]
            
    for rec in record:
        rec_chunk = rec.split()
        if rec_chunk[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %name_history[rec_chunk[1]])
        elif rec_chunk[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %name_history[rec_chunk[1]])
            
    return(answer)