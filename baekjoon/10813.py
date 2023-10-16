N, M = map(int, input().split())
basket = []
for p in range(1, N+1):
    basket.append(p)

for p in range(M):
    i, j = map(int, input().split())
    x = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = x

for p in range(N):
    print(basket[p], end=' ')