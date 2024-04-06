a, b = map(int, input().split())

answer = float("inf")

def dfs(x, k):
    global answer
    if x > b:
        return
    if x == b:
        if k < answer:
            answer = k
    for i in range(2):
        if i == 0:
            dfs(2*x, k+1)
        if i == 1:
            dfs(x*10+1, k+1)

dfs(a, 1)

if answer == float("inf"):
    print(-1)
else:
    print(answer)