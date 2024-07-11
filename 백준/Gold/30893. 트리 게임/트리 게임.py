from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, s, e = map(int, input().split())

graph = [[] for i in range(n+1)]
for t in range(n-1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
visited[s] = True
answer = [-1] * (n+1)

def dfs(node):
    cnt = 0
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            visited[i] = False
            if answer[node] < answer[i]:
                answer[node] = answer[i]
        else:
            cnt += 1

    if cnt == len(graph[node]):
        if not visited[e]:
            answer[node] = 0
        else:
            answer[node] = 1

dfs(s)

q = deque()
q.append([s, 1])
vvisited = [False] * (n+1)
vvisited[s] = True

flag = True
while q:
    node, seq = q.popleft()

    cnt = 0
    for i in graph[node]:
        if seq == 1:
            if not vvisited[i] and answer[i] == 1:
                vvisited[i] = True
                q.append([i, 2])
        else:
            if not vvisited[i]:
                if answer[i] == 0:
                    flag = False
                    break
                vvisited[i] = True
                q.append([i, 1])

    if not flag:
        break

if not vvisited[e]:
    flag = False

if flag:
    print("First")
else:
    print("Second")