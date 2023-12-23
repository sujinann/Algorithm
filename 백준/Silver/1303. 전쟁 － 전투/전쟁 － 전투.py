from collections import deque
m, n = map(int, input().split())
maps = []
for i in range(n):
    maps.append(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False]*m for i in range(n)]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    cnt = 1

    temp = maps[x][y]
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == temp and not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1

    return cnt

a, b = 0, 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            c = bfs(i, j)
            if maps[i][j] == 'W':
                a += c**2
            else:
                b += c**2

print(a, b)