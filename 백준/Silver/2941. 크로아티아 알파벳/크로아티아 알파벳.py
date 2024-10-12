word = input()
cr_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cr_a:
    word = word.replace(i, '*')

print(len(word))
