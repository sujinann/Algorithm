from collections import deque


N, M = map(int, input().split())
maze = []
for _ in range(N):
  maze.append(list(map(int, input())))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

q = deque()
q.append([0, 0])

while q:
    r, c = q.popleft()
    


    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]


        if 0<=nr<N and 0<=nc<M and maze[nr][nc] == 1:
            maze[nr][nc] = maze[r][c] + 1
            q.append([nr, nc])
            

print(maze[N-1][M-1])