from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
l = []
p = deque()


vvisited = [[False]*c for i in range(r)]

for i in range(r):
    line = list(input())
    graph.append(line)
    for j in range(len(line)):
        if line[j] == 'L':
            vvisited[i][j] = True
            l.append([i, j])
            p.append([i, j]) 
        elif line[j] == '.':
            vvisited[i][j] = True
            p.append([i, j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False]*c for i in range(r)]

xx = l[0][0]
yy = l[0][1]

a = l[1][0]
b = l[1][1]

visited[xx][yy] = True

q = deque()
q.append([xx, yy])

def check():
    global q

    nq = deque()
    # for i in range(len(dq)):
    #     q.append(dq[i])

    

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'X':
                nq.append([x, y])
                continue
            if not visited[nx][ny]:
                if nx == a and ny == b:
                    return True
                visited[nx][ny] = True
                q.append([nx, ny])


    q = nq
    return False



def melt():
    global p
    np = deque()

    while p:
        x, y = p.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if graph[nx][ny] == 'X' and not vvisited[nx][ny]:
                vvisited[nx][ny] = True
                graph[nx][ny] = '.'
                np.append([nx, ny])

    p = np


cnt = 0
while True:
    if check():
        print(cnt)
        break
    
    cnt += 1
    melt()