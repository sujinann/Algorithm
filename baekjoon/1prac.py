def dfs(studnet):
    global graph
    global visited
    global combilist
    global cnt

    for i in graph[studnet]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)

def solution(n, nationality):
    global graph
    global visited
    global combilist
    global cnt

    answer = -1

    graph = [[] for i in range(n+1)]

    for i in nationality:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    combilist = []

    visited = [False] * (n+1)

    for i in range(1, n+1):
        if len(graph[i]) == 0:
            combilist.append(1)

        else:
            for j in graph[i]:
                
                if not visited[j]:
                    visited[j] = True
                    cnt = 1
                    dfs(j)
                    combilist.append(cnt)

    print(combilist)

    return answer

solution(4, [[1,2], [2,3], [1,3]])