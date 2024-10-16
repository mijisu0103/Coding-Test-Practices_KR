cnt = 0

def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)
    
def isPal(s):
    global cnt
    cnt = 0
    return recursion(s, 0, len(s)-1)

t = int(input())
for i in range(t):
    s = input()
    print(isPal(s), cnt)