INF = float('INF')
def solution(n, s, a, b, fares):
    distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in fares:
        distance[i[0]][i[1]] = i[2]
        distance[i[1]][i[0]] = i[2]
    
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    distance[i][j] = 0
                elif distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    answer = INF
    for i in range(1, n + 1):
        answer = min(answer, distance[s][i] + distance[i][a] + distance[i][b])
    return answer