from collections import deque


w, h = map(int, input().split())
maps = []
c = []
for i in range(h):
    maps.append(list(input()))

    for j in range(w):
        if maps[i][j] == 'C':
            c.append([i, j])
        if maps[i][j] == '.':
            maps[i][j] = -1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

x = c[0][0]
y = c[0][1]

maps[x][y] = 0
maps[c[1][0]][c[1][1]] = -1

q = deque()
q.append([x, y, 0])

visited = [[[0, 0] for j in range(w)] for i in range(h)]
visited[x][y] = [1, 1]

while q:
    temp = q.popleft()
    x = temp[0]
    y = temp[1]
    answer = temp[2]
    
    for i in range(4):
        k = 0
        while True:
            k += 1
            nx = x + (dx[i] * k)
            ny = y + (dy[i] * k)

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                break

            if maps[nx][ny] == '*':
                break

            if maps[nx][ny] != -1:
                if maps[nx][ny] < answer:
                    break
            
                if maps[nx][ny] == answer:
                    if visited[nx][ny][i%2] == 1:
                        break

            maps[nx][ny] = answer
            visited[nx][ny][i%2] = 1

            if maps[c[1][0]][c[1][1]] != -1:
                break

            q.append([nx, ny, maps[nx][ny]+1])

    if maps[c[1][0]][c[1][1]] != -1:
        break

print(maps[c[1][0]][c[1][1]])