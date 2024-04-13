import sys
input = sys.stdin.readline

n = int(input())

inp = [[] for i in range(n**2+1)]

dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]

maps = [[0] * n for i in range(n)]
visited = [[] for i in range(n**2+1)]

def second_req(target):
    maxi = -1
    point = []
    for x in range(n):
        for y in range(n):
            if maps[x][y] == 0:
                cnt = 0
                for i in range(4):
                    nx = x + dir[i][0]
                    ny = y + dir[i][1]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    if maps[nx][ny] == 0:
                        cnt += 1

                if cnt > maxi:
                    maxi = cnt
                    point = [x, y]

    maps[point[0]][point[1]] = target
    visited[target] = [point[0], point[1]]



def first_req(target, likes):
    check = [[0] * n for i in range(n)]

    ords = []
    for l in likes:
        if len(visited[l]) > 0:
            ords.append(visited[l])
    
    if len(ords) == 0:
        second_req(target)
    else:
        maxi = 0
        like_list = []
        for o in ords:
            x = o[0]
            y = o[1]
            for i in range(4):
                nx = x + dir[i][0]
                ny = y + dir[i][1]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if maps[nx][ny] == 0:
                    check[nx][ny] += 1

                    if check[nx][ny] > maxi:
                        maxi = check[nx][ny]
                        like_list = [[nx, ny]]
                    elif check[nx][ny] == maxi:
                        like_list.append([nx, ny])



        if len(like_list) == 0:
            second_req(target)
        else:
            like_list.sort()
            maxi = 0
            point = [like_list[0][0], like_list[0][1]]
            for k in like_list:
                x = k[0]
                y = k[1]
                cnt = 0

                for i in range(4):
                    nx = x + dir[i][0]
                    ny = y + dir[i][1]

                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    if maps[nx][ny] == 0:
                        cnt += 1

                if cnt > maxi:
                    maxi = cnt
                    point = [x, y]

            maps[point[0]][point[1]] = target
            visited[target] = [point[0], point[1]]




for i in range(n**2):
    l = list(map(int, input().split()))
    inp[l[0]] = l[1:]

    if i == 0:
        maps[1][1] = l[0]
        visited[l[0]] = [1, 1]

    else:
        first_req(l[0], l[1:])

answer = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if maps[nx][ny] in inp[maps[x][y]]:
                cnt += 1

        if cnt != 0:
            answer += 10**(cnt-1)

print(answer)