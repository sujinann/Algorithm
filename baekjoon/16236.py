from collections import deque

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

fish = [0] * 7

for i in range(N):
    for j in range(N):
        if 1 <= arr[i][j] <= 6:
            fish[arr[i][j]] += 1
        elif arr[i][j] == 9:
            start = [i, j]
            arr[i][j] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

now = 2

answer = 0

targetcount = fish[1]

def bfs(s, w):
    global answer
    global start
    global arr

    visited = [[-1] * N for i in range(N)]

    q = deque()
    q.append([s, w])
    visited[s[0]][s[1]] = 0

    while q:
        s, w = q.popleft()
        x = s[0]
        y = s[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    if arr[nx][ny] == w or arr[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([[nx, ny], w])
                    elif arr[nx][ny] != 0 and arr[nx][ny] < w:
                        visited[nx][ny] = visited[x][y] + 1
    
    maxi = N**2

    nnx = -1
    nny = -1

    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] < w:
                if 0 < visited[i][j] < maxi:
                    maxi = visited[i][j]
                    nnx = i
                    nny = j

    if nnx != -1:

        answer += maxi
        arr[nnx][nny] = 0
        start = [nnx, nny]
        

c = 0

while targetcount != 0:

    t = start
    bfs(start, now)
    if start == t:
        break

    c += 1
    targetcount -= 1

    if c == now:
        now += 1
        c = 0
        if now <= 7:
            targetcount += fish[now - 1]

print(answer)