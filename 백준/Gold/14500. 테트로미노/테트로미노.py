n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = []

def dfs(node, graph, visited, s, t):
    if len(visited) == 4:
        answer.append(s)
        return
    
    x = node[0]
    y = node[1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        nnode = [nx, ny]

        if nnode not in visited:
            visited.append(nnode)
            dfs(nnode, graph, visited, s+graph[nx][ny], t)
            visited.pop()
        else:
            if len(visited) == 3 and t == 0:
                dfs(nnode, graph, visited, s, t+1)
            
for i in range(n):
    for j in range(m):
        dfs([i, j], graph, [[i,j]], graph[i][j], 0)

print(max(answer))