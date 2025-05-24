import sys
input = sys.stdin.readline

N = int(input())
change = 1000 - N
money = [500, 100, 50, 10, 5, 1]
answer = 0

for mon in money:
    if change == 0:
        break
    
    answer += change // mon
    change %= mon
    
print(answer)
