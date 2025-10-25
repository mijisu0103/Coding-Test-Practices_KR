def to_days(date):
    y, m, d = map(int, date.split("."))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    today = to_days(today)
    
    term = dict()
    for t in terms:
        type_, period = t.split()
        term[type_] = int(period) * 28
    
    for idx, p in enumerate(privacies):
        numb = idx + 1
        date, type_ = p.split()
        
        if to_days(date) + term[type_] - 1 < today:
            answer.append(numb)
    
    return answer