def solution(s):
    
    nums = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
        'zero':0
    }
    
    for i in nums:
        if i in s:
            s = s.replace(i, str(nums[i]))
    
    print(s)
            
    return int(''.join(s))