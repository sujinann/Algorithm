N, M = map(int, input().split())
basket = list(range(1, N+1))

for p in range(M):
    i, j = map(int, input().split())
    tmp=basket[i-1:j]
    tmp.reverse()
    basket[i-1:j] = tmp

for p in range(N):
    print(basket[p], end=' ')