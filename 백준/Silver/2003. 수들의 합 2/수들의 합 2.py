N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

start = 0
end = 0
sum = A[0]

count = 0

while True:
    if sum == M:
        count += 1
        
    if sum >= M:
        start += 1
        sum -= A[start - 1]
    else:
        if end == N - 1:
            break
        end += 1
        sum += A[end]

print(count)