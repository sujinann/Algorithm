n = int(input())
k = int(input())
l = list(map(int, input().split()))
l.sort()

dist = []
for i in range(n-1):
    dist.append(l[i+1] - l[i])

dist.sort()
print(sum(dist[:n-k]))
