def solution(friends, gifts):
    answer = 0
    n = len(friends)
    
    friend_dict = dict()
    for i in range(n):
        friend_dict[friends[i]] = i
        
    table = [[0] * n for _ in range(n)]
    
    gift_indices = [0] * n
    
    for gift in gifts:
        a, b = gift.split()
        idx1, idx2 = friend_dict[a], friend_dict[b]
        gift_indices[idx1] += 1
        gift_indices[idx2] -= 1
        table[idx1][idx2] += 1
    
    
    get_gift = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if table[i][j] > table[j][i]:
                get_gift[i] += 1
            elif table[i][j] == table[j][i]:
                if gift_indices[i] > gift_indices[j]:
                    get_gift[i] += 1
    
    answer = max(get_gift)
    return answer