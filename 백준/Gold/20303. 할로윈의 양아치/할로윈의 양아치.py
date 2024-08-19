import sys
sys.setrecursionlimit(10**9)

n, m, k = map(int, input().split())
c = list(map(int, input().split()))

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(x):
    global cnt, value
    if visited[x]:
        return
    
    visited[x] = True
    cnt += 1
    value += c[x-1]

    for i in graph[x]:
        if not visited[i]:
            dfs(i)

temp = []
for i in range(1, n+1):
    cnt = 0
    value = 0
    if not visited[i]:
        dfs(i)
    if cnt > 0:
        temp.append([cnt, value])

dp = [[0]*k for i in range(len(temp)+1)]
for i in range(1, len(temp)+1):
    for j in range(1, k):
        if temp[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-temp[i-1][0]] + temp[i-1][1])

print(dp[len(temp)][k-1])