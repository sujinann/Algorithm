n, m = map(int, input().split())
answer = 0

maps = []
target = []

def change(x, y):
    for i in range(3):
        for j in range(3):
            if maps[x+i][y+j] == 0:
                maps[x+i][y+j] = 1
            else:
                maps[x+i][y+j] = 0

for i in range(n):
        maps.append(list(map(int, input())))
for i in range(n):
    target.append(list(map(int, input())))

if n < 3 or m < 3:
    for i in range(n):
        for j in range(m):
            if maps[i][j] != target[i][j]:
                answer = -1
                break
        if answer == -1:
            break
else:

    for i in range(n):
        for j in range(m):
            if i <= n-3 and j <= m-3:
                if maps[i][j] != target[i][j]:
                    change(i, j)
                    answer += 1
            else:
                if maps[i][j] != target[i][j]:
                    answer = -1
                    break

        if answer == -1:
            break

print(answer)