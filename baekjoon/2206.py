from collections import deque


n, m = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited = [[False]*m for i in range(n)]

def bfs(x, y, cnt, p):
    q = deque()
    q.append([x, y, cnt, p])
    maps[x][y] = cnt

    while q:
        x, y, cnt, p = q.popleft()
        if x == n-1 and y == m-1:
            if cnt > 0:
                return cnt
            else:
                return -cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if p == 0:
                    if maps[nx][ny] <= 0 and not visited[nx][ny]:
                        maps[nx][ny] = cnt + 1
                        q.append([nx, ny, cnt+1, p])

                    if maps[nx][ny] == 1:
                        maps[nx][ny] = -cnt - 1
                        visited[nx][ny] = True
                        q.append([nx, ny, -cnt-1, p+1])
                
                else:
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = cnt-1
                        q.append([nx, ny, cnt-1, p])

    return -1

print(bfs(0, 0, 1, 0))