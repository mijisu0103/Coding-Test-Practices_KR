from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for i in permutations(dungeons, len(dungeons)):
        temp = k
        cnt = 0
        for req, dam in i:
            if temp >= req:
                temp -= dam
                cnt += 1
        answer = max(cnt, answer)
    return answer