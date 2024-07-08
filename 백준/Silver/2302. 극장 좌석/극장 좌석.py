n = int(input())
m = int(input())

step = []
start = 1
for i in range(m):
    k = int(input())
    step.append(k - start)
    start = k + 1
step.append(n+1 - start)

dp = [1] * 41
dp[2] = 2

for i in range(3, 41):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
for s in step:
    answer *= dp[s]

print(answer)