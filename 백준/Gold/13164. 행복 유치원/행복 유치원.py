n, k = map(int, input().split())

l = list(map(int, input().split()))

answer = []
for i in range(1, n):
    answer.append(l[i] - l[i-1])

answer.sort()
print(sum(answer[:n-k]))