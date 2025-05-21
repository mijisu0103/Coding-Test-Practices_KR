def solution(s):
    
    lst = []
    
    for i in s.split("},"):
        lst.append(i.replace("{", "").replace("}", "").split(","))
    
    lst.sort(key = len)
    answer=[]
    
    for i in lst:
        for j in i:
            if j not in answer:
                answer.append(j)
                
    return list(map(int, answer))