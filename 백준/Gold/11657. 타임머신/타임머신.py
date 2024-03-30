n, m = map(int, input().split())
INF = float("INF")
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

time = [INF] * (n+1)
time[1] = 0

for repeat in range(n):
    for i in range(1, n+1):
        for j in graph[i]:
            node = j[0]
            cost = j[1]
            C = time[i] + cost
            if time[i] != INF and time[node] > C:
                time[node] = C
                if repeat == n-1:
                    print(-1)
                    exit()

for i in range(2, n+1):
    if time[i] == INF:
        print(-1)
    else:
        print(time[i])