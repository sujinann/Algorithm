n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []

def dfs(x, y, visited, path, cnt, t):
    if cnt == 3:
        answer.append(path)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if [nx, ny] not in visited:
                visited.append([nx, ny])
                dfs(nx, ny, visited, path + graph[nx][ny], cnt+1, t)
                visited.pop()
            else:
                if cnt == 2 and t == 0:
                    dfs(nx, ny, visited, path, cnt, t+1)

for i in range(n):
    for j in range(m):
        dfs(i, j, [[i, j]], graph[i][j], 0, 0)

print(max(answer))