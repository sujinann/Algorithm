from collections import deque


t = int(input())

def bfs(x, y):
    global answer
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(len(graph[x])):
            if visited[graph[x][i]] == 0:
                visited[graph[x][i]] = -y
                q.append([graph[x][i], visited[graph[x][i]]])

            else:
                if visited[graph[x][i]] == y:
                    answer = "NO"
                    break
        if answer == "NO":
            break

for tc in range(t):
    a, b = map(int, input().split())

    graph = [[] for i in range(a+1)]
    visited = [0]*(a+1)

    for i in range(b):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = "YES"


    for i in range(1, a+1):
        if visited[i] == 0:
            visited[i] = 1
            bfs(i, visited[i])
        else:
            bfs(i, visited[i])

    print(answer)