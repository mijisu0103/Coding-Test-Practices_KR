def solution(schedules, timelogs, startday):
    answer = 0
    
    allowed_time = []
    cnt = 0
    
    for s in schedules:
        
        h = int(s) // 100
        m = (int(s) % 100 % 60) + 10
        
        if m >= 60:
            m %= 60
            h += 1
        
        allowed_time.append(h*100+m)
    
    # 주말 제외
    for i in range(len(schedules)):
        for t in range(len(timelogs[i])):

            if (t+startday)%7 == 0 or (t+startday)%7 == 6:
                timelogs[i][t] = 2359
    
    for i in range(len(schedules)):
        for t in timelogs[i]:
            if int(allowed_time[i]) >= int(t):
                cnt += 1

        if cnt == 5:
            answer += 1
        cnt = 0
                            
    return answer