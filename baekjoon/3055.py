from collections import deque


r, c = map(int, input().split())

maps = []
for i in range(r):
    maps.append(list(map(str, input())))

water = []
start = []
dest = []
for i in range(r):
    for j in range(c):
        if maps[i][j] == "*":
            water.append([i, j])
        elif maps[i][j] == "S":
            start = [i, j]
        elif maps[i][j] == "D":
            dest = [i, j]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0]*c for i in range(r)]

answer = "KAKTUS"

q = deque()
q.append(start)
for i in water:
    q.append(i)

while q:
    x, y = q.popleft()

    if maps[x][y] == "S":
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny] == ".":
                    maps[nx][ny] = "S"
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                elif maps[nx][ny] == "D":
                    answer = visited[x][y] + 1
                    break
                
        if answer != "KAKTUS":
            break
    
    elif maps[x][y] == "*":
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny] == "." or maps[nx][ny] == "S":
                    maps[nx][ny] = "*"
                    q.append([nx, ny])

print(answer)