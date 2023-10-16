n = int(input())
numlist = list(map(int, input().split()))
dp = [0]*n
sum = [0]*n

start = 0

for i in range(n):
    sum[i] = sum(numlist[start : i+1])
    if sum[i] 

print(max(dp))