T = int(input())
N, L = map(int, input().split())

hamburgers = []

for i in range(N):
    hamburgers.append(list(map(int, input().split())))

answer = 0

def dfs(idx, f, c):
    global answer
    if c > L:
        return
    
    if f > answer:
        answer = f

    if idx == N:
        return

    dfs(idx+1, f + hamburgers[idx][0], c + hamburgers[idx][1])
    dfs(idx+1, f, c)

dfs(0, 0, 0)

print(answer)