M = int(input())
N = int(input())
ans = []
a = 0
for i in range(M, N + 1):
    cnt = 0
    if i > 1:
        for p in range(2, i):
            if i % p == 0 :
                cnt += 1
        if cnt == 0:
            ans.append(i)
            a += 1
if a == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])