n, m = map(int, input().split())
basket = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    for i in range(i, j+1):
        basket[i-1] = k
        
for _ in range(n):
    basket = map(str,basket)
    print(" ".join(basket))