n = int(input())
m = int(input())

INF = float('INF')

graph = [[INF] * n for i in range(n)]
route = [[[] for i in range(n)] for i in range(n)]

for i in range(n):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())

    if c < graph[a-1][b-1]:
        graph[a-1][b-1] = c
        route[a-1][b-1] = [a, b]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                route[i][j] = route[i][k][:-1] + route[k][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(n):
    print(*graph[i])

for i in range(n):
    for j in range(n):
        print(len(route[i][j]), *route[i][j])