import sys
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

answer = 0

for i in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

cnt = 0
def dfs(x, y):
    global s

    visited[x] = True

    if y < s:
        s = y

    for i in range(len(graph[x])):
        if not visited[graph[x][i]]:
            dfs(graph[x][i], a[graph[x][i]-1])

for i in range(1, n+1):
    if not visited[i]:
        s = 10001
        dfs(i, a[i-1])
        answer += s

if k >= answer:
    print(answer)
else:
    print("Oh no")