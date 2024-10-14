n = int(input())
num = []

for i in range(n):
    num.append(int(input()))
num2 = sorted(num)

for i in range(len(num)):
    print(num2[i])