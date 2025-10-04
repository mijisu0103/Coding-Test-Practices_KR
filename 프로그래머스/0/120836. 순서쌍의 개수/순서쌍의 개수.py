def solution(n):

    lst = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
        if i ** 2 == n:
            lst.append(i)

    return(len(lst) - 1 if int((n ** 0.5)) == n / (n ** 0.5) else len(lst))
