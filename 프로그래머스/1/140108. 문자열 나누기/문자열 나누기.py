def solution(s):
    cnt1, cnt2, ans, x = 0, 0, 0, ""

    for i in s:
        if cnt1 == cnt2:
            cnt1 += 1
            x = i
            ans += 1
        elif i == x:
            cnt1 += 1
        else:
            cnt2 += 1
            
    return ans