def solution(polynomial):
    
    answer = ''
    
    coeff = 0
    const = 0

    terms = polynomial.split(' + ')
    
    for term in terms:
        term = term.strip()
        
        if 'x' in term:
            if term == 'x':
                coeff += 1
            elif term == '-x':
                coeff -= 1
            else:
                coeff += int(term[:-1])
        else:
            const += int(term)
        
    if coeff != 0:
        if coeff == 1:
            answer += 'x'
        elif coeff == -1:
            answer += '-x'
        else:
            answer += f'{coeff}x'
    
    if const != 0:
        if answer:
            answer += f' + {const}'
        else:
            answer += str(const)

    return answer