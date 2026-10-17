def solution(name, yearning, photo):
    answer = []
    score_dict = dict(zip(name, yearning))

    for p in photo:
        score = 0
        for person in p:
            score += score_dict.get(person, 0)
        answer.append(score)

    return answer