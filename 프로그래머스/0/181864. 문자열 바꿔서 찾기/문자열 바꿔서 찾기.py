def solution(myString, pat):
    
    change = myString.maketrans('AB', 'BA')
    myString = myString.translate(change)
    
    return 1 if pat in myString else 0