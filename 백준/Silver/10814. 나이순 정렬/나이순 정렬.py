n = int(input())

l = []

for _ in range(n):
    age, name = input().split()
    l.append([int(age), name])
    
l.sort(key = lambda x: int(x[0]))

for i in l:
    print(i[0], i[1])