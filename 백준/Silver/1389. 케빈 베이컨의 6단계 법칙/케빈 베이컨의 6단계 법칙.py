n, m = map(int, input().split())
INF = float('INF')

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
            break

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
maxi = INF

for i in range(1, n+1):
    if maxi > sum(graph[i][1:]):
        answer = i
        maxi = sum(graph[i][1:])

print(answer)