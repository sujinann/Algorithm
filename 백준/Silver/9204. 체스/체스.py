tc = int(input())

dir = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(x, y, d):
    global visit
    visit[x][y] = True

    nx = x + d[0]
    ny = y + d[1]

    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        return

    dfs(nx, ny, d)

def search(x, y, d):
    global visit
    global stop
    global flag

    if visit[x][y]:
        stop = [x, y]
        flag = True
        return

    nx = x + d[0]
    ny = y + d[1]

    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        return

    search(nx, ny, d)


for t in range(tc):
    answer = "Impossible"
    st, rt, e, nd = input().split()

    st = ord(st) - ord('A')
    rt = int(rt) - 1
    e = ord(e) - ord('A')
    nd = int(nd) - 1

    if (st+rt)%2 != (e+nd)%2:
        print(answer)
    else:
        visit = [[False] * 8 for i in range(8)]
        flag = False
        for d in dir:
            dfs(st, rt, d)

        for d in dir:
            search(e, nd, d)
            if flag:
                break
        
        if st == e and rt == nd:
            answer = [0, chr(st+ord('A')), rt+1]
        else:
            if (stop[0] == st and stop[1] == rt) or (stop[0] == e and stop[1] == nd):
                answer = [1, chr(st+ord('A')), rt+1, chr(e+ord('A')), nd+1]
            else:
                answer = [2, chr(st+ord('A')), rt+1, chr(stop[0]+ord('A')), stop[1]+1, chr(e+ord('A')), nd+1]

        print(*answer)
