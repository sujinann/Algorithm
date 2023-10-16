N = int(input())
L = []
for i in range(N):
    L.append(int(input()))
ans = sorted(L)
for i in range(N):
    print(ans[i])