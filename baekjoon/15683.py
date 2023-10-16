import copy


n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

cctv = []

for i in range(n):
    for j in range(m):
        if 1<= maps[i][j] <=5:
            cctv.append([maps[i][j], i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

type = [
    [[0], [1], [2], [3]], 
    [[2, 3], [0, 1]], 
    [[0, 2], [1, 3], [0, 3], [1, 2]],
    [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]],
    [[0, 1, 2, 3]]
    ]

def watch(board, x, y, t):
    for d in t:
        nx = x
        ny = y
        
        while True:
            nx += dx[d]
            ny += dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    board[nx][ny] = -1
                elif board[nx][ny] == 6:
                    break
                else:
                    continue

answer = 64

# def dfs(cnt, maps):
#     global answer
#     if cnt == len(cctv):
#         cntz = 0
#         for i in range(n):
#             for j in range(m):
#                 if maps[i][j] == 0:
#                     cntz += 1

#         if cntz < answer:
#             answer = cntz
#         return

    
#     for tt in type[cctv[cnt][0]-1]:
#         temp = copy.deepcopy(maps)
#         watch(temp, cctv[cnt][1], cctv[cnt][2], tt)
#         dfs(cnt+1, temp)
        
def dfs(cnt, arr):
    global answer
    if cnt == len(cctv):
        cntz = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cntz += 1

        if cntz < answer:
            answer = cntz
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[cnt]
    for tt in type[cctv_num - 1]:
        
        watch(temp, x, y, tt)
        dfs(cnt + 1, temp)
        temp = copy.deepcopy(arr)

dfs(0, maps)
print(answer)