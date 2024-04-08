import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [1] * (n+1)
for i in range(1, k):
    dp = [sum(dp[0:j+1]) for j in range(n+1)]

print(dp[-1] % 1000000000)