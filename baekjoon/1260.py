import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

graph2 = graph
l = len(graph)
visited = [False] * (N+1)
answer = []

def dfs(V):
    visited[V] = True
    answer.append(V)

    for i in range(len(graph[V])):
        if not visited[graph[V][i]]:
            dfs(graph[V][i])

dfs(V)
print(*answer)


visited2 = [False] * (N+1)
answer2 = []


q = deque()
q.append(V)
visited2[V] = True

while q:
    t = q.popleft()
    answer2.append(t)
    for i in range(len(graph2[t])):
        if not visited2[graph2[t][i]]:
            visited2[graph2[t][i]] = True
            x = graph2[t][i]
            q.append(x)
           
print(*answer2)