t = int(input())
for i in range(t):
    stamp = []
    n = int(input())
    dp = [[0]*n for i in range(2)]

    for j in range(2):
        stamp.append(list(map(int, input().split())))
    
    dp[0][0] = stamp[0][0]
    dp[1][0] = stamp[1][0]

    if n > 1:
        dp[0][1] = stamp[1][0] + stamp[0][1]
        dp[1][1] = stamp[0][0] + stamp[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stamp[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + stamp[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))