n = int(input())
k = int(input())
l = list(map(int, input().split()))
l.sort()

dist = [l[i+1] - l[i] for i in range(n-1)]

dist.sort()
print(sum(dist[:n-k]))