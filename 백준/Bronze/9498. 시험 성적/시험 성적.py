n = int(input())
p='A'
if n<60:
    p='F'
elif n<70:
    p='D'
elif n<80:
    p='C'
elif n<90:
    p='B'
else:
    p='A'
print(p)