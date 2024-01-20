import sys
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for i in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

visited = [-1] * (n+1)
answer = 0

def dfs(x, y):
        
    for i in range(len(graph[x])):
        if visited[graph[x][i][0]] == -1:
            visited[graph[x][i][0]] = y + graph[x][i][1]
            dfs(graph[x][i][0], y + graph[x][i][1])
            
visited[1] = 0
dfs(1, 0)

m = 0
temp = -1
for i in range(n+1):
    if visited[i] > temp:
        temp = visited[i]
        m = i

visited = [-1] * (n+1)
visited[m] = 0
dfs(m, 0)

answer = max(visited)

print(answer)