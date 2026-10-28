def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}
    
    for c in callings:
        idx = result[c]
        result[c] -= 1
        result[players[idx-1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
    
    return players