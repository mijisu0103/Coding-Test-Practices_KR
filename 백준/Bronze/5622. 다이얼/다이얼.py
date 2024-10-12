dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
char = list(input())
result = 0

for i in char:
    for j in dial:
        if i in str(j):
            time = dial.index(j) + 3
            result += time
            
print(result)