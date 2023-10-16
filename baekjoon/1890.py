n = int(input())
m = []

for i in range(n):
    m.append(list(map(int, input().split())))

dp = [[0]*n for i in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        
        if j + m[i][j] < n:
            dp[i][j + m[i][j]] += dp[i][j]
        if i + m[i][j] < n:
            dp[i + m[i][j]][j] += dp[i][j]
        
        if i == n - 1 and j == n - 2:
            break

print(dp[n-1][n-1])