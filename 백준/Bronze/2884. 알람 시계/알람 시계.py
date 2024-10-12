h,m = map(int, input().split())
    
hm = h*60 + m
hm -= 45
    
if hm < 0:
    hm += 24*60
        
print(hm // 60, hm % 60)