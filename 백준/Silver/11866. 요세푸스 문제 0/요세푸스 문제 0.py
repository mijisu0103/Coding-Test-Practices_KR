import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = [i for i in range(1, n+1)]
josephus = [0] * n

kill = k
del_num = k-1
josephus[0] = nums[del_num]
nums.remove(kill)

for m in range(1, n):
    nums_length = len(nums)
    del_num += (k-1)
    del_num %= nums_length
    josephus[m] = nums[del_num]
    nums.remove(nums[del_num])
    
print('<', end='') 
for f in range(n-1):
    print(josephus[f], end=', ')
print(josephus[-1], end='')
print('>')