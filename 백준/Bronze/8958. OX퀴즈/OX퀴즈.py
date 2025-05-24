n = int(input())

for i in range(0, n):
    count, c = 0, 1
    s = list(input())
    
    for j in s:
        if j == 'O':
            count += c
            c += 1
            
        else:
            c = 1
            
    print(count)