import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

directions_x = [0, 0, -1, -1, -1, 0, 1, 1, 1]
directions_y = [0, -1, -1, 0, 1, 1, 1, 0, -1]

clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for i in range(m):
    d, s = map(int, input().split())
    visited = []
    visited_map = [[False] * n for k in range(n)]
    for cloud in clouds:
        nx = (cloud[0] + (directions_x[d] * s)) % n
        ny = (cloud[1] + (directions_y[d] * s)) % n

        maps[nx][ny] += 1
        visited.append([nx, ny])
        visited_map[nx][ny] = True

    for v in visited:
        cnt = 0
        for j in range(1, 5):
            nnx = v[0] + directions_x[2*j]
            nny = v[1] + directions_y[2*j]

            if nnx < 0 or nny < 0 or nnx >= n or nny >= n:
                continue

            if maps[nnx][nny] > 0:
                cnt += 1

        maps[v[0]][v[1]] += cnt

    clouds = []
    for p in range(n):
        for q in range(n):
            if maps[p][q] >= 2 and not visited_map[p][q]:
                maps[p][q] -= 2
                clouds.append([p, q])

answer = 0
for i in range(n):
    answer += sum(maps[i])

print(answer)