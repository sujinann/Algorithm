dp = []

for i in range(100000):
    dp.append(i)

def find_square(m, n):
    ans = 0
    len = min(m, n)
    for i in range(1, len + 1):
        ans += (m - i + 1) * (n - i + 1) * dp[i]
    print(ans)

while True:
    m, n = map(int, input().split())
    if (m == 0 and n == 0): exit()
    find_square(m, n)

    temp = 0
    for i in range(1, min(m, n) + 1):
        temp += (m - i + 1) * (n - i + 1) * i
    print(temp)