from collections import deque


n, m = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(str, input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, visited, cnt):
    q = deque()
    q.append([x, y, cnt])
    visited[x][y] = True
    

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny] == "L":
                visited[nx][ny] = True
                q.append([nx, ny, cnt+1])

    return cnt

answer = 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == "L":
            visited = [[False] * m for k in range(n)]
            temp = bfs(i, j, visited, 0)
            if temp > answer:
                answer = temp

print(answer)