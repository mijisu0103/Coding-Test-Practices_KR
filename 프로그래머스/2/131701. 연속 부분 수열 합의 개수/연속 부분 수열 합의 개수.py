def solution(elements):
    
    n = len(elements)
    result = set()

    elements = elements * 2 

    prefix_sum = [0] * (2 * n + 1)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = prefix_sum[i - 1] + elements[i - 1]

    for length in range(1, n + 1):
        for start in range(n):
            end = start + length
            sub_sum = prefix_sum[end] - prefix_sum[start]
            result.add(sub_sum)

    return len(result)
