import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

tmap = []
for i in range(n):
    tmap.append(list(map(int, input().rstrip().split())))

dp = [[0]*m for i in range(n) ]
dp [0][0] = 1

def move(x, y):
    if x <= n-2 and tmap[x][y] > tmap[x+1][y]:
        dp[x+1][y] += 1
        move(x+1, y)
    if 0 < x and tmap[x][y] > tmap[x-1][y]:
        dp[x-1][y] += 1
        move(x-1, y)
    if y <= m-2 and tmap[x][y] > tmap[x][y+1]:
        dp[x][y+1] += 1
        move(x, y+1)
    if 0 < y and tmap[x][y] > tmap[x][y-1]:
        dp[x][y-1] += 1
        move(x, y-1)

move(0, 0)
print(dp[n-1][m-1])
print(dp)

