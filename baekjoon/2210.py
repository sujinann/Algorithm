from collections import deque


maps = []
for i in range(5):
    maps.append(list(map(str, input().split())))

answer = set()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y, temp):
    global answer
    q = deque()
    temp += maps[x][y]
    q.append([x, y, temp])


    while q:
        x, y, temp = q.popleft()

        if len(temp) == 6:
            answer.add(temp)
        
        if len(temp) == 7:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<5 and 0<=ny<5:
                newtemp = temp + maps[nx][ny]
                q.append([nx, ny, newtemp])

for i in range(5):
    for j in range(5):
        bfs(i, j, "")

print(len(answer))