def solution(mats, park):
    
    max_y, max_x = len(park), len(park[0])
    
    for mat in sorted(mats, reverse=True):
        for y in range(max_y - mat + 1):
            for x in range(max_x - mat + 1):
                success = True
                for cur_y in range(y, y + mat):
                    for cur_x in range(x, x + mat):
                        if park[cur_y][cur_x] != '-1':
                            success = False
                            break
                    if not success:
                        break
                if success:
                    return mat
    return -1