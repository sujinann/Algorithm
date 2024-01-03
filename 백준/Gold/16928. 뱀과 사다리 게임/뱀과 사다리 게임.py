from collections import deque


n, m = map(int, input().split())

graph = [i for i in range(101)]
visited = [0] * 101

for i in range(n + m):
    x, y = map(int, input().split())
    graph[x] = y

q = deque()
q.append(1)
visited[1] = 1

answer = 20

while q:
    v = q.popleft()

    if v == 100:
        if visited[100] - 1 < answer:
            answer = visited[100] - 1
    elif v > 100:
        continue

    for i in range(1, 7):
        g = v + i
        if g <= 100:
            if visited[graph[g]] == 0:
                visited[graph[g]] = visited[v] + 1
                q.append(graph[g])

print(answer)