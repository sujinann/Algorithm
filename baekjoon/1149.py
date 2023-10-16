n = int(input())
dp = [[0]*3 for i in range(n+1)]

rlist = [0]
glist = [0]
blist = [0]

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    rlist.append(r)
    glist.append(g)
    blist.append(b)

dp[1][0] = rlist[1]
dp[1][1] = glist[1]
dp[1][2] = blist[1]

for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rlist[i]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + glist[i]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + blist[i]

print(min(dp[n]))