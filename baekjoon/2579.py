n = int(input())
stair = [0]
for i in range(1, n+1):
    stair.append(int(input()))
dp = [0]*(n+1)

if n <= 2:
    print(sum(stair))
else:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    
    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])

    print(dp[n])