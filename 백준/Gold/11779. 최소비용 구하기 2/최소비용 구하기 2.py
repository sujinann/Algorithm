import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

INF = float('INF')
graph = [[INF, []] for _ in range(n + 1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    graph[start] = [0, [start]]
    while q:
        d, now = heapq.heappop(q)
        if graph[now][0] < d:
            continue
        for next, val in edges[now]:
            if graph[next][0] > d + val:
                graph[next][0] = d + val
                graph[next][1] = graph[now][1] + [next]
                heapq.heappush(q, (d+val, next))

start, end = map(int, input().split())
dijkstra(start)
print(graph[end][0])
print(len(graph[end][1]))
print(*graph[end][1])