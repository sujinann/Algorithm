N, K = map(int, input().split())
list = []
cnt = 0
for i in range(1, N + 1):
    if N % i == 0:
        list.append(i)
        cnt += 1
if cnt >= K:
    print(list[K-1])
else :
    print(int(0))