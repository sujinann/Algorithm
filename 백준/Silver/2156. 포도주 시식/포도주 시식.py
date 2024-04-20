n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

dp = [[0] * n for i in range(3)]
if n <= 2:
    answer = sum(l)
else:
    dp[1][0] = l[0]
    dp[0][1] = l[0]
    dp[1][1] = l[1]
    dp[2][1] = l[0] + l[1]
    for i in range(2, n):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = dp[0][i-1] + l[i]
        dp[2][i] = dp[1][i-1] + l[i]

    answer = max(dp[0][n-1], dp[1][n-1], dp[2][n-1])

print(answer)