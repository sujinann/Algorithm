n, k = map(int, input().split())
coins = []
for i in range(n):
    coin = int(input())
    coins.append(coin)

answer = 0
for i in range(len(coins)):
    if len(coins) > 0:
        if coins[len(coins)-i-1] <= k:
            answer += k // coins[len(coins)-i-1]
            k %= coins[len(coins)-i-1]
            if k == 0:
                break

print(answer)