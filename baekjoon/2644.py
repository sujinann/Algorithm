from collections import deque


n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)

q = deque()
cnt = 0
q.append([a, cnt])
visited[a] = True

while q:
    temp, cnt = q.popleft()
    if temp == b:
        break

    for i in range(len(graph[temp])):
        if not visited[graph[temp][i]]:
            q.append((graph[temp][i], cnt+1))
            visited[graph[temp][i]] = True

if cnt == 0 or not visited[b]:
    print(-1)
else:
    print(cnt)