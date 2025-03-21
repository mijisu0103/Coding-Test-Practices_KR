from itertools import product

def solution(word):
    alps = ["A", "E", "I", "O", "U"]
    words = []

    for i in range(1, 6):
        for p in product(alps, repeat=i):
            words.append("".join(p))
    
    words.sort()

    return words.index(word) + 1
