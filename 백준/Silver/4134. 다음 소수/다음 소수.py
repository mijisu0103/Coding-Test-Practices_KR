import sys, math
input = sys.stdin.readline

def is_Prime(x):
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True

n = int(input())

for _ in range(n):
    x = int(input())
    while(1):
        if is_Prime(x) == True:
            print(x)
            break
        else:
            x+=1