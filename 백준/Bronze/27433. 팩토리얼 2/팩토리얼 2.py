n = int(input())

def IsFact(n):
    if n <= 1:
        ans = 1
    else:
        ans = IsFact(n-1) * n
        
    return ans

print(IsFact(n))