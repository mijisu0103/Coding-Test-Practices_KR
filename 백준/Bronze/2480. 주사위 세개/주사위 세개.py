n1, n2, n3 = map(int, input().split())

prize = 0

if n1 == n2 and n1 == n3:
    prize = 10000 + n1 * 1000
elif n1 != n2 and n1 != n3 and n2 != n3:
    dn = n1
    if dn < n2:
        dn = n2
    if dn < n3:
        dn = n3
    prize = dn * 100
else:
    dn = n1
    if n2 == n3:
        dn = n2
    prize = 1000 + dn * 100

print(prize)