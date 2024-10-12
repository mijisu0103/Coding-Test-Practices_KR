for i in range(9):
    n = int(input())
    if i == 0:
        max = n
        p = 1
    else:
        if max < n:
            max = n
            p = i + 1
          
print(max, p, sep="\n")