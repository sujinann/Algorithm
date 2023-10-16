from collections import deque


F, S, G, U, D = map(int, input().split())

q = deque()
q.append([S, 0])

visited = [False] * (F+1)
visited[S] = True

while q:
    x, cnt = q.popleft()
    if x == G:
        break

    for i in [x+U, x-D]:
        if 0<i<=F and not visited[i]:
            visited[i] = True
            q.append([i, cnt+1])

if cnt >= 0 and visited[G]:
    print(cnt)
else:
    print("use the stairs")