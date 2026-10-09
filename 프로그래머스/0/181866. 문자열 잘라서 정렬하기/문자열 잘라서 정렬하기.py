def solution(myString):
    answer = []
    spr = sorted(myString.split("x"))
    
    for i in spr:
        if i.isalpha()==True:
            answer.append(i)
    
    return answer