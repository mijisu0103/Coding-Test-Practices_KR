s1 = input()
s2 = input()

n1 = int(s1)
n2_1 = int(s2[2])
n2_10 = int(s2[1])
n2_100 = int(s2[0])

n3 = n1 * n2_1
n4 = n1 * n2_10
n5 = n1 * n2_100

n6 = n3 + 10*n4 + 100*n5

print(n3, n4, n5, n6, sep="\n")