from collections import deque


n, m = map(int, input().split())
graph = []
flag = False
start = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

    if not flag:
        for j in range(len(temp)):
            if temp[j] == 2:
                flag = True
                start = [i, j]
                break

visited = [[False] * m for i in range(n)]
q = deque()
q.append([start[0], start[1], 0])
visited[start[0]][start[1]] = True
answer = [[0] * m for i in range(n)]

dir = [[0,1],[1,0],[-1,0],[0,-1]]

while q:
    x, y, v = q.popleft()
    
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if visited[nx][ny] or graph[nx][ny] == 0:
            continue

        q.append([nx, ny, v+1])
        visited[nx][ny] = True
        answer[nx][ny] = v+1

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if graph[i][j] > 0:
                answer[i][j] = -1

for i in range(n):
    print(*answer[i])