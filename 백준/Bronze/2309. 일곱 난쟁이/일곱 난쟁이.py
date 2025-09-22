from itertools import combinations

heights = []

for _ in range(9):
    height = int(input())
    heights.append(height)
    
for a in combinations(heights, 7):
    if sum(a) == 100:
        a = list(a)
        a.sort()
        for x in a:
            print(x)
        break