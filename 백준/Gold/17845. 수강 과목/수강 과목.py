n, k = map(int, input().split())
l = []
for i in range(k):
    l.append(list(map(int, input().split())))
    
dp = [[0] * (n+1) for i in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if l[i-1][1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i-1][1]] + l[i-1][0])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[k][n])