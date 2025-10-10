def solution(quiz):
    answer = []
    
    for i in quiz:
        i = i.split('=')
        if '- ' in i[0]:
            i[0] = i[0].split('- ')
            answer.append('O' if int(i[0][0]) - int(i[0][1]) == int(i[1]) else 'X')
        else:
            i[0] = i[0].split('+')
            answer.append('O' if int(i[0][0]) + int(i[0][1]) == int(i[1]) else 'X')

    return answer