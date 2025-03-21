from collections import deque

# 두 단어 사이 다른 글자 개수 확인
def check(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
           cnt += 1
    return cnt
    
def solution(begin, target, words):
    answer = 0
    

    if target not in words:
        return 0
    

    q = deque()
    q.append((begin, 0))
    
    while q:
        n_word, times = q.popleft()
        if n_word == target:
            return times
        
        for word in words:
            change = check(word, n_word)
            if change == 1:
                q.append((word, times + 1))