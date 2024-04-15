from collections import deque


n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(x, y, v):
    q = deque([[x, y]])
    cnt = 1
    total = graph[x][y]
    visited[x][y] = v

    while q:
        x, y = q.popleft()

        for d in dir:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] >= 0:
                continue

            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                q.append([nx, ny])
                visited[nx][ny] = v
                cnt += 1
                total += graph[nx][ny]

    if cnt == 1:
        visited[x][y] = -1

    return cnt, total//cnt

answer = 0
while True:
    visited = [[-1] * n for i in range(n)]
    score = []
    flag = False
    for x in range(n):
        for y in range(n):
            if visited[x][y] < 0:
                c, s = bfs(x, y, len(score))
                if c > 1:
                    score.append(s)
                    flag = True

    if not flag:
        break

    for x in range(n):
        for y in range(n):
            if visited[x][y] >= 0:
                graph[x][y] = score[visited[x][y]]

    answer += 1

print(answer)