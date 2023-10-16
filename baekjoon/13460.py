from collections import deque

n, m = map(int, input().split())

board = []
r = [0, 0]
b = [0, 0]
for i in range(n):
    line = list(map(str, input()))
    board.append(line)
    for j in range(len(line)):
        if line[j] == 'R':
            r = [i, j]
        elif line[j] == 'B':
            b = [i, j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def move(x, y, dirx, diry):
    cnt = 0
    while board[x + dirx][y + diry] != '#' and board[x][y] != 'O':
        cnt += 1
        x += dirx
        y += diry
    return x, y, cnt

q = deque()
q.append([r[0], r[1], b[0], b[1], 0])
visited = []
answer = -1

while q:
    rx, ry, bx, by, cnt = q.popleft()

    if cnt < 10:
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    answer = cnt + 1
                    break

                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if [nrx, nry, nbx, nby] not in visited:
                    visited.append([nrx, nry, nbx, nby])
                    q.append([nrx, nry, nbx, nby, cnt+1])

    if answer != -1:
        break

print(answer)