n = int(input())

answer = []

visited = [False] * (n+1)
def dfs(r, dep):
    if dep == n:
        answer.append(r)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            dfs(r+[i], dep+1)
            visited[i] = False
            
dfs([], 0)    
        
for a in answer:
    print(*a)