def solution(ingredient):
    stack = []
    answer = 0

    for x in ingredient:
        stack.append(x)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()

    return answer