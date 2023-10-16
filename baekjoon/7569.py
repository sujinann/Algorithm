from collections import deque


m, n, h = map(int, input().split())

maps = []
for i in range(h):
    floor = []
    for j in range(n):
        floor.append(list(map(int, input().split())))
    maps.append(floor)


dx = [0,0,-1,1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,-1,1]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 1:
                q.append([j, k, i, 0])

cnt = 0
while q:
    x, y, z, cnt = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0<=nx<n and 0<=ny<m and 0<=nz<h and maps[nz][nx][ny] == 0:
            maps[nz][nx][ny] = 1
            q.append([nx, ny, nz, cnt+1])

answer = cnt

for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 0:
                answer = -1
                break
        if answer == -1:
            break
    if answer == -1:
        break

print(answer)