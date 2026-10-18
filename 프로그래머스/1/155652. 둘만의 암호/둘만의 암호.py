def solution(s, skip, index):
    answer = ""
    
    a = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in skip]

    for char in s:
        cur_loc = a.index(char)
        cur_loc += index
        re_loc = cur_loc % len(a)
        answer += a[re_loc]

    return answer