def dfs(idx):
    global answer

    if len(select) == m:
        val = 0

        for h in house:
            dist = 2*n
            for c in select:
                temp = abs(h[0] - c[0]) + abs(h[1] - c[1])
                if temp < dist:
                    dist = temp
            val += dist
        
        if val < answer:
            answer = val

        return

    for i in range(idx, k):
        select.append(chicken[i])
        dfs(i+1)
        select.pop()


n, m = map(int, input().split())

maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append([i, j])
        elif maps[i][j] == 2:
            chicken.append([i, j])

select = []

k = len(chicken)
answer = 2*n*len(house)

dfs(0)

print(answer)