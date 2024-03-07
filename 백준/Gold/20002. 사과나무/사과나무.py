import sys
input = sys.stdin.readline

n = int(input())
maps = []
for i in range(n):
    temp = list(map(int, input().split()))
    maps.append(temp)
dp = [[0] * (n+1) for i in range(n+1)]

answer = -1000

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + maps[i-1][j-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(n):
            if i+k > n:
                continue
            if j+k > n:
                continue
            s = dp[i+k][j+k] - dp[i-1][j+k] - dp[i+k][j-1] + dp[i-1][j-1]
            if s > answer:
                answer = s

print(answer)