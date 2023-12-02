t = int(input())
for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    scores = [0]*n
    score = 0
    for i in range(n):
        if l.count(l[i]) >= 6:
            score += 1
            scores[i] = score
        else:
            scores[i] = 0

    maps = [[0, 0, 0, i] for i in range(n+1)]
    for i in range(n):
        if maps[l[i]][2] < 4:
            maps[l[i]][0] += scores[i]
        elif maps[l[i]][2] == 4:
            maps[l[i]][1] = maps[l[i]][0] + scores[i]

        maps[l[i]][2] += 1

    answer = []

    for i in range(n+1):
        if maps[i][0] != 0:
            answer.append(maps[i])

    answer.sort(key= lambda x : (x[0], x[1]))
    print(answer[0][3])