n = int(input())
enter = str(input())
cnt = 0
dic = {}

for i in range(1, n):
    word = str(input())
    if word == 'ENTER':
        for key, value in dic.items():
            if value == 1:
                cnt += 1
        dic = {}
        continue
    if word not in dic:
        dic[word] = 1

for key, value in dic.items():
    if value == 1:
        cnt += 1

print(cnt)