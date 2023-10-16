import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = [[] for i in range(N+1)]

for i in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    

visited = [0]*(N+1)

def dfs(x):
    for i in range(len(graph[x])):
        if visited[graph[x][i]] == 0:
            visited[graph[x][i]] = x
            dfs(graph[x][i])

dfs(1)

for i in range(2, N+1):
    print(visited[i])