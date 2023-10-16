from collections import deque



r, c = map(int, input().split())

maps = []
for i in range(r):
    maps.append(list(map(str, input())))

water = []
start = []
for i in range(r):
    for j in range(c):
        if maps[i][j] == "F":
            water.append([i, j])
        elif maps[i][j] == "J":
            start = [i, j]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0]*c for i in range(r)]

answer = "IMPOSSIBLE"

q = deque()
q.append(start)
for i in water:
    q.append(i)

while q:
    x, y = q.popleft()


    if maps[x][y] == "J":
        if x == 0 or x == r-1 or y == 0 or y == c-1:
            answer = visited[x][y] + 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny] == ".":
                    maps[nx][ny] = "J"
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([nx, ny])
                
    
    elif maps[x][y] == "F":
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c:
                if maps[nx][ny] == "." or maps[nx][ny] == "J":
                    maps[nx][ny] = "F"
                    q.append([nx, ny])

if start[0] == 0 or start[0] == r-1 or start[1] == 0 or start[1] == c-1:
    answer = 1

print(answer)