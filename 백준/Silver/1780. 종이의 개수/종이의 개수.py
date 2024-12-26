import sys

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,sys.stdin.readline().split())))

result = {-1:0, 0:0,1:0}

def divided(row,col,n):
    curr = paper[row][col]

    for i in range(row, row+n):
        for j in range(col, col+n):
            if paper[i][j] != curr:
                next = n//3

                divided(row, col, next)
                divided(row, col+next, next)
                divided(row, col+(next*2), next)
                divided(row+next, col, next)
                divided(row+next, col+next, next)
                divided(row+next, col+(next*2), next)
                divided(row+(next*2), col, next) 
                divided(row+(next*2), col+next, next)
                divided(row+(next*2), col+(next*2), next) 
                return 


    result[curr] +=1 
    return 


divided(0,0,n)

for i in result.values():
    print(i)