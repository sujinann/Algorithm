from collections import deque


N = int(input())
maps = []
maxi = 0

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] > maxi:
            maxi = maps[i][j]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(a, b, v, visited):
    q = deque()
    q.append([a, b])
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]

            if 0<=nr<N and 0<=nc<N and maps[nr][nc] > v and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append([nr, nc])


answer = 0

for k in range( maxi):
    visited = [[False] * N for i in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if maps[r][c] > k and not visited[r][c]:
                bfs(r, c, k, visited)
                
    
                cnt += 1

    if cnt > answer:
        answer = cnt

print(answer)