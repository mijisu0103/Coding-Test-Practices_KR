from collections import defaultdict

def solution(tickets):
    
    graph = defaultdict(list)
    
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route = []
    
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop(0))
        route.append(airport)
    
    dfs("ICN")
    return route[::-1]

