n = int(input())
cnt = 0
answer = 0
board = [[0]*n for i in range(n)]

def dfs(n):
    global cnt
    global answer
    if cnt == n:
        answer += 1
        return
    for i in range(n):
        for j in range(n):
            if sum(board[i]) == 0:
                s = 0
                for k in range(n):
                    s += board[k][j]
                if s == 0:
                    t = 0
                    m = max(i, j)
                    mi = min(i, j)
                    for l in range(mi):
                        t += board[i-l][j-l]
                    for l in range(n-m):
                        t += board[i+l][j+l]
                    t += board[i][j]
                    if t == 0:
                        p = 0
                        for r in range(n+1):
                            if i-r>=0 and j+r<n:
                                p += board[i-r][j+r]
                        for r in range(n+1):
                            if i+r<n and j-r>=0:
                                p+= board[i+r][j-r]
                        if p == 0:
                            board[i][j] = 1
                            cnt+=1
                            dfs(n)
                            cnt-=1
                            board[i][j] = 0

dfs(n)
print(answer)