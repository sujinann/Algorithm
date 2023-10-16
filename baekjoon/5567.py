from collections import deque

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append([1, 0])
answer = 0
visited = [False] * (n+1)
visited[1] = True

while q:
    x, cnt = q.popleft()

    if cnt < 2:
        for i in range(len(graph[x])):
            if not visited[graph[x][i]]:
                visited[graph[x][i]] = True
                q.append([graph[x][i], cnt+1])
                answer += 1

print(answer)