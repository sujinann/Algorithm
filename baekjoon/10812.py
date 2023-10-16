N, M = map(int, input().split())
l = []
for p in range(1, N+1):
    l.append(p)

for p in range(M):
    i, j, k = map(int, input().split())
    temp1 = l[k-1 : j]
    temp2 = l[i-1 : k-1]
    
    l = l[ : i-1] + temp1 + temp2 + l[j : ]

for p in range(N):
    print(l[p], end=' ')