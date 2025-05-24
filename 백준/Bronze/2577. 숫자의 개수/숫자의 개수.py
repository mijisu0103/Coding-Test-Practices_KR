A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))

for i in range(0, 10):
    cnt = 0
    
    for num in result:
        if i == int(num):
            cnt += 1
            
    print(cnt)