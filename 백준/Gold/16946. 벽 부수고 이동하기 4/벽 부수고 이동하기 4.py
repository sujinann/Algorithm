from collections import deque

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))

answer = [[0] * m for i in range(n)]
visited = [[False] * m for i in range(n)]

dir = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True

    ordinate = set()
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1

        for d in dir:
            nx = x + d[0]
            ny = y + d[1]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            if maps[nx][ny] == 1:
                ordinate.add((nx, ny))
            else:
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True

    for o in ordinate:
        answer[o[0]][o[1]] += cnt

for x in range(n):
    for y in range(m):
        if maps[x][y] == 1:
            answer[x][y] += 1
        else:
            if not visited[x][y]:
                bfs(x, y)

trans_answer = []
for x in range(n):
    temp = ''
    for y in range(m):
        temp += str(answer[x][y] % 10)
    trans_answer.append(temp)

for a in trans_answer:
    print(a)