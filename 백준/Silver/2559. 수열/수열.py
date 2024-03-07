n, k = map(int, (input().split()))
l = list(map(int, input().split()))

answer = [0] * (n-k+1)

for i in range(k):
    answer[0] += l[i]

for i in range(1, n-k+1):
    answer[i] = answer[i-1] - l[i-1] + l[i+k-1]

print(max(answer))