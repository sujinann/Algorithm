from collections import deque


N, K = map(int, input().split())

q = deque()
q.append([N, 0])

visited = [False] * (100001)

while q:
    x, cnt = q.popleft()

    if x == K:
        break

    if not visited[x]:
        visited[x] = True
        if x-1>=0:
            q.append([x-1, cnt+1])
        if x+1<=100000:
            q.append([x+1, cnt+1])
        if 2*x<=100000:
            q.append([2*x, cnt+1])

print(cnt)