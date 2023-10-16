N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in A:
    cnt = 0
    if i > 1:
        for p in range(2, i):
            if i % p == 0:
                cnt += 1
        if cnt == 0:
            ans += 1
    else :
        continue
print(ans)