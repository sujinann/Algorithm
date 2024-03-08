n, l = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

answer = 0

for i in range(n):
    way = True
    for j in range(n):
        if j == 0:
            pre = maps[i][j]
            cnt = 1
        else:
            if maps[i][j] - pre == 0:
                cnt += 1
                if not way:
                    if cnt >= l:
                        way = True
                        cnt = 0
            elif maps[i][j] - pre == 1:
                if not way:
                    break
                if cnt >= l:
                    cnt = 1
                    pre += 1
                else:
                    way = False
                    break
            elif maps[i][j] - pre == -1:
                if not way:
                    break
                way = False
                cnt = 1
                if cnt >= l:
                    way = True
                    cnt = 0
                pre -= 1
            else:
                way = False
                break

    if way:
        answer += 1



for j in range(n):
    way = True
    for i in range(n):
        if i == 0:
            pre = maps[i][j]
            cnt = 1
        else:
            if maps[i][j] - pre == 0:
                cnt += 1
                if not way:
                    if cnt >= l:
                        way = True
                        cnt = 0
            elif maps[i][j] - pre == 1:
                if not way:
                    break
                if cnt >= l:
                    cnt = 1
                    pre += 1
                else:
                    way = False
                    break
            elif maps[i][j] - pre == -1:
                if not way:
                    break
                way = False
                cnt = 1
                if cnt >= l:
                    way = True
                    cnt = 0
                pre -= 1
            else:
                way = False
                break

    if way:
        answer += 1

print(answer)