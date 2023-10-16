n, k = map(int, input().split())
s, a = 1, 1
for i in range(k):
    s *= n-i
for i in range(k):
    a *= k-i
print(s//a)