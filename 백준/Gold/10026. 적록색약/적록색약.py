import sys
sys.setrecursionlimit(10**9)

n = int(input())
maps = []
for i in range(n):
    maps.append(list(input()))

visited = [[False] * n for i in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(x, y):
    if visited[x][y]:
        return
    
    visited[x][y] = True

    for d in dir:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if maps[x][y] != maps[nx][ny]:
            continue

        dfs(nx, ny)

answer = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer += 1
            dfs(i, j)

for i in range(n):
    for j in range(n):
        if maps[i][j] == 'G':
            maps[i][j] = 'R'


answer2 = 0
visited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer2 += 1
            dfs(i, j)

print(answer, answer2)