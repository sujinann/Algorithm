n, k = map(int, input().split())
l = list(map(int, input().split()))

a = 2**20
x = 0

while a >= 1:
    temp = []
    for i in l:
        if i & a:
            temp.append(i)

    if len(temp) >= k:
        x |= a
        l = temp

    a //= 2

print(x)