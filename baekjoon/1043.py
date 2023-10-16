from collections import deque


n, m = map(int, input().split())
know = list(map(int, input().split()))[1:]

party = [[] for i in range(n+1)]
templ = []

for i in range(m):    
    temp = list(map(int, input().split()))[1:]
    templ.append(temp)
    if len(temp) > 1:
        for j in range(len(temp)-1):
            for k in range(j+1, len(temp)):
                party[temp[j]].append(temp[k])
                party[temp[k]].append(temp[j])

visited = [False]*(n+1)

q = deque()
for i in range(len(know)):
    q.append(know[i])
    visited[know[i]] = True

while q:
    x = q.popleft()

    for i in range(len(party[x])):
        if not visited[party[x][i]]:
            q.append(party[x][i])
            visited[party[x][i]] = True


atemp = []
for i in range(1, n+1):
    if visited[i] == True:
        atemp.append(i)

cnt = 0
for i in range(m):
    for j in range(len(templ[i])):
        if templ[i][j] in atemp:
            cnt += 1
            break

answer = m - cnt
print(answer)