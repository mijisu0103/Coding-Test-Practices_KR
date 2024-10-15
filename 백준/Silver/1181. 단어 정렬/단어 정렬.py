n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

set_arr = set(arr)
l = list(set_arr)
l.sort()
l.sort(key = len)

for i in l:
    print(i)

