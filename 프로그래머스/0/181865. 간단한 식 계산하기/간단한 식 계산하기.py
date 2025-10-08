def solution(binomial):
    
    op = ['+', '-', '*']
    
    answer = ''
    
    for i in op:
        if i in binomial:
            bi = binomial.split(i)
            
            if i == '+':
                answer = int(bi[0]) + int(bi[1])
                
            elif i == '-':
                answer = int(bi[0]) - int(bi[1])
                
            else:
                answer = int(bi[0]) * int(bi[1])
                
    return answer