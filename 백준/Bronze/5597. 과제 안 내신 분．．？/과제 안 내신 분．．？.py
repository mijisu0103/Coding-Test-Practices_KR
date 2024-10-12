sn = [0]*31

for i in range(28):
    v = int(input())
    sn[v] = 1
    
for i in range(1, 31):
    if sn[i] == 0:
        print(i)