def solution(a, b):
    
    answer = []
    
    i = len(a) - 1
    j = len(b) - 1
    
    carry = 0

    while i >= 0 or j >= 0 or carry:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0

        total = x + y + carry
        answer.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(reversed(answer))