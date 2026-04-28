def solution(keyinput, board):
    
    answer = [0, 0]
    
    max_x, max_y = board[0] // 2, board[1] // 2
    min_x, min_y = -(board[0] // 2), -(board[1] // 2)
    
    for k in keyinput:
        if k == "left" and answer[0] > min_x:
            answer[0] -= 1
        elif k == "right" and answer[0] < max_x:
            answer[0] += 1
        elif k == "down" and answer[1] > min_y:
            answer[1] -= 1
        elif k == "up" and answer[1] < max_y:
            answer[1] += 1
    
    return answer