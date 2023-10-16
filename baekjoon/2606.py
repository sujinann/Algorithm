com = int(input())
n = int(input())

graph = [[] for i in range(com+1)]
visited = [False]*(com+1)

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def dfs(c):
    global cnt
    visited[c] = True
    for i in range(len(graph[c])):
        if not visited[graph[c][i]]:
            cnt += 1
            dfs(graph[c][i])

dfs(1)

print(cnt)