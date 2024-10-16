ans = []

for i in range(int(input())):
    arr = list(input().split())
    if "ChongChong" in arr:
        ans.extend(arr)
        continue
    for j in arr:
        if j in ans:
            ans.extend(arr)
print(len(set(ans)))