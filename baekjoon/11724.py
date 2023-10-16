from collections import deque


n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
cnt = 1
answer = 0
while cnt != 0:
    cnt = 0
    answer += 1
    for i in range(n+1):
        if graph[i] != []:
            q.append([i, graph[i]])
            cnt = 1
            break

    temp, templist = q.popleft()
