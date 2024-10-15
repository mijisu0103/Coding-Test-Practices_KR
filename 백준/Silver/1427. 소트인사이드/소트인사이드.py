n = int(input())

l = []

for i in str(n):
    l.append(int(i))
    
l.sort(reverse=True)

for i in l:
    print(i, end='')