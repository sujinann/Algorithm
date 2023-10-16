N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
A = []
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for p in range(j+1, N):
            if L[i] + L[j] + L[p] <= M:
                A.append(L[i]+L[j]+L[p])
ans = sorted(A)
print(max(ans))