n = int(input())

arr = list(map(int, input().split()))
max_dp = arr
min_dp = arr

for i in range(1, n):
    arr = list(map(int, input().split()))
    max_dp = [arr[0]+max(max_dp[0:2]), arr[1]+max(max_dp), arr[2]+max(max_dp[1:3])]
    min_dp = [arr[0]+min(min_dp[0:2]), arr[1]+min(min_dp), arr[2]+min(min_dp[1:3])]

print(max(max_dp), end=" ")
print(min(min_dp))