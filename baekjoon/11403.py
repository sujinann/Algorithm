from collections import deque
 
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
 
def bfs(x):
    queue = deque()
    queue.append(x)
    
 
    while queue:
        q = queue.popleft()
 
        for i in range(n):
            if visited[x][i] == 0 and graph[q][i] == 1:
                queue.append(i)
                
                visited[x][i] = 1
 
for i in range(n):
    bfs(i)
 
for i in visited:
    print(*i)