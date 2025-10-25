from collections import defaultdict

def solution(fees, records):
    answer = []
    rec_map = defaultdict(list)
    
    for rec in records:
        time = int(rec.split()[0].split(':')[0]) * 60 + int(rec.split()[0].split(':')[1])
        car_num = rec.split()[1]
        
        rec_map[car_num].append(time)
    
    rec_map = dict(sorted(rec_map.items()))

    for v in rec_map.values():
        if len(v) % 2 != 0:
            v.append(23 * 60 + 59)
        
        total_time = sum(v[i + 1] - v[i] for i in range(0, len(v), 2))
        
        if total_time <= fees[0]:
            answer.append(fees[1])
        else:
            extra_time = total_time - fees[0]
            extra_fee = (extra_time // fees[2]) * fees[3]
            
            if extra_time % fees[2] != 0:
                extra_fee += fees[3]
            answer.append(fees[1] + extra_fee)

    return answer