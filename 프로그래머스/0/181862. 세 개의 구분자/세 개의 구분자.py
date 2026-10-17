def solution(myStr):
    for x in ['a', 'b', 'c']:
        myStr = myStr.replace(x, ' ')
    
    answer = myStr.split()
    return answer if answer else ['EMPTY']