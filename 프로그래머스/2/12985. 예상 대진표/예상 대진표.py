def solution(N, A, B):
    round = 0 
    while A != B:
        round += 1
        A = (A + 1) // 2
        B = (B + 1) // 2
    return round