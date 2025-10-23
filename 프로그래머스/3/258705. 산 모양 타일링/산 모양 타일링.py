def solution(n, tops):
    
    MOD = 10007
    a = 1
    b = 2 + tops[0]

    for i in range(1, n):
        na = (a + b) % MOD
        nb = (a * (1 + tops[i]) + b * (2 + tops[i])) % MOD
        a, b = na, nb

    return (a + b) % MOD