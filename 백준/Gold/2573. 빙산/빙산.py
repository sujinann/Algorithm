from collections import deque


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for i in range(n)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    global visited
    q = deque([[x, y]])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for d in dir:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue

            if graph[nx][ny] > 0:
                q.append([nx, ny])
                visited[nx][ny] = True


def sep():
    global visited
    visited = [[False] * m for i in range(n)]
    cnt = 0

    for x in range(1, n-1):
        for y in range(1, m-1):
            if graph[x][y] > 0 and not visited[x][y]:
                cnt += 1
                if cnt > 1:
                    return True
                bfs(x, y)

    if cnt == 0:
        print(0)
        exit()
    return False

def melt():
    global memo
    plus = []
    for x in range(1, n-1):
        for y in range(1, m-1):
            if graph[x][y] > 0:
                graph[x][y] -= memo[x][y]
                if graph[x][y] < 0:
                    graph[x][y] = 0
                if graph[x][y] == 0:
                     for d in dir:
                        nx = x + d[0]
                        ny = y + d[1]

                        plus.append([nx, ny])
    
    for p in plus:
        memo[p[0]][p[1]] += 1



memo = [[0] * m for i in range(n)]
for x in range(1, n-1):
    for y in range(1, m-1):
        if graph[x][y] > 0:
            cnt = 0
            for d in dir:
                nx = x + d[0]
                ny = y + d[1]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if graph[nx][ny] == 0:
                    cnt += 1

            memo[x][y] = cnt

answer = 0
while True:
    if sep():
        break
    melt()
    answer += 1
    
print(answer)