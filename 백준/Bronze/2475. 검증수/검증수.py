l = list(map(int, input().split()))

s = 0
for i in range(5):
    s += (l[i] % 10) ** 2

print(s % 10)