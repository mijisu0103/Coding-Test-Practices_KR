import sys

input = sys.stdin.readline
N = int(input()) 

status = [list(map(int,input().split())) for _ in range(N)]

visited = [False] * N
result = sys.maxsize 

def dfs(a, idx):
    global result
    
    if a == N // 2 : 
    	
        team_start = 0
        team_link = 0
        
        for i in range (N):
            for j in range (N):
            	
                if visited[i] and visited[j]: 
                    team_start += status[i][j]
                    
                elif not visited[i] and not visited[j]: 
                    team_link += status[i][j]
        
        result = min(result, abs(team_start-team_link))
        return
        
    else:
        for i in range(idx, N):
            if not visited[i]:
                visited[i] = True
                dfs(a+1, i+1)
                visited[i] = False

dfs (0,0)
print(result)