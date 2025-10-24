def solution(dartResult):
    scores = []
    
    power_dict = { 'S' : 1, 'D' : 2, 'T' : 3 }
    option_dict = { '*' : 2, '#' : -1 }

    dartResult = dartResult.replace('10', 'K')

    for s in dartResult:
        if s.isdigit():
            scores.append(int(s))
        else:
            if s == 'K':
                scores.append(10)
            elif s in power_dict:
                scores[-1] **= power_dict[s]
            else:
                if s == '*':
                    scores[-2:] = [x * 2 for x in scores[-2:]]
                else:
                    scores[-1] *= option_dict[s]

    return sum(scores)