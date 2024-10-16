n = int(input())

for _ in range(n):
    ps = input()
    stack = []

    for i in ps:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')