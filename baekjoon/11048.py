n, m = map(int, input().split())
maze = []

dp = [[0]*m for i in range(n)]

for i in range(n):
    maze.append(list(map(int, input().split())))

dp[0][0] = maze[0][0]

for i in range(1, m):
    dp[0][i] = maze[0][i] + dp[0][i-1]

for i in range(1, n):
    dp[i][0] = maze[i][0] + dp[i-1][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + maze[i][j]

print(dp[n-1][m-1])