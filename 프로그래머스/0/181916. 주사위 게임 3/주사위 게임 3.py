def solution(a, b, c, d):
    answer = 0
    lst = [a, b, c, d]
    arr = list(set(lst))
    
    # 모두 다르면 min of a, b, c, d
    if len(arr) == 4:
        answer = min(arr)
    
    # 두개 p, 다른 주사위 q, r => q x r
    elif len(arr) == 3:
        p = max(lst, key = lst.count)
        tmp = [num for num in arr if num != p]
        answer = tmp[0] * tmp[1]
    
    # 세개 p, 다른거 q => (10 x p + q)**2
    # 두개씩 같은 값, p, q => (p+q) x |p-q|
    elif len(arr) == 2:
        if max([lst.count(num) for num in arr]) > 2:
            p = max(lst, key = lst.count)
            q = min(lst, key = lst.count)
            answer = ((10 * p) + q) ** 2
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))  

    # 4개 다 p => 1111 x p
    elif len(arr) == 1:
        answer = int(str(arr[0]) * 4)

    return answer