t = int(input())

for i in range(t):
    m, n, x, y = map(int, input().split())
    cnt = 0
    while x <= m*n:
        if (x-y) % n == 0:
            cnt = 1
            print(x)
            break
        x += m
    
    if cnt == 0:
        print(-1)