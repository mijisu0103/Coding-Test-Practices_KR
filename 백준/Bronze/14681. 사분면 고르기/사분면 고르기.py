x = int(input())
y = int(input())

n = 4

if x > 0 and y > 0:
    n = 1
elif x < 0 and y > 0:
    n = 2
elif x < 0 and y < 0:
    n = 3
elif x > 0 and y < 0:
    n = 4

print(n)