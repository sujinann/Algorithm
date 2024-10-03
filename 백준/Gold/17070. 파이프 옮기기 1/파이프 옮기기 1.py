import sys
input = sys.stdin.readline

n = int(input())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

if maps[n-1][n-1] == 1:
    print(0)
    exit()
    
dir = [(0, 1), (1, 1), (1, 0)]

answer = 0

def dfs(x, y, d):
    global answer
    
    for i in range(3):
        if d == 0 and i == 2:
            continue

        if d == 2 and i == 0:
            continue

        nx = x + dir[i][0]
        ny = y + dir[i][1]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if maps[nx][ny] == 1:
            continue

        if i == 1:
            if maps[nx][ny-1] == 1 or maps[nx-1][ny] == 1:
                continue

        if nx == n - 1 and ny == n - 1:
            answer += 1

        dfs(nx, ny, i)

dfs(0, 1, 0)
print(answer)