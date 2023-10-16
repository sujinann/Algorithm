from collections import deque

n, k, m = map(int, input().split())
graph = [[] for i in range(n+m+1)]

for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        graph[temp[j]].append(n+i+1)
        graph[n+i+1].append(temp[j])

visited = [False] * (n+m+1)

q = deque()
q.append([1, 1])
visited[1] = True

answer = -1

while q:
    x, cnt = q.popleft()
    if x == n:
        answer = cnt - cnt//2
        break

    for i in range(len(graph[x])):
        if not visited[graph[x][i]]:
            q.append([graph[x][i], cnt+1])
            visited[graph[x][i]] = True

print(answer)



# 위 풀이는 mk

# 메모리초과 풀이 mkk
# from collections import deque

# n, k, m = map(int, input().split())

# graph = [[] for i in range(n+1)]

# for i in range(m):
#     temp = list(map(int, input().split()))
#     for j in range(len(temp)-1):
#         for k in range(j+1, len(temp)):
#             graph[temp[j]].append(temp[k])
#             graph[temp[k]].append(temp[j])

# visited = [False] * (n+1)

# q = deque()
# q.append([1, 1])
# visited[1] = True

# answer = -1

# while q:
#     x, cnt = q.popleft()
#     if x == n:
#         answer = cnt
#         break

#     for i in range(len(graph[x])):
#         if not visited[graph[x][i]]:
#             visited[graph[x][i]] = True
#             q.append([graph[x][i], cnt+1])

# print(answer)