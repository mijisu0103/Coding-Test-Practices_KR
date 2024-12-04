import sys

n = int(sys.stdin.readline())
cnt = 0
columns = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

def queen(a):
    global cnt
    if a == n:
        cnt += 1
        return
    for i in range(n):
        if not columns[i] and not diag1[a - i + n - 1] and not diag2[a + i]:
            columns[i] = diag1[a - i + n - 1] = diag2[a + i] = True
            queen(a + 1)
            columns[i] = diag1[a - i + n - 1] = diag2[a + i] = False

queen(0)
print(cnt)
