a, b = map(int, input().split())
c, d = map(int, input().split())
x = a*d + c*b
y = b*d
n = min(x, y)
m = int(n**0.5)
l = [True]*(n+1)
for i in range(2, m+1):
    if l[i] == True:
        for j in range(i*2, n+1, i):
            l[j] = False
l2 = set()
for i in range(2,n+1):
    if l[i] == True:
        l2.add(i)

for i in l2:
    while x%i == 0 and y%i == 0:
        x = x//i
        y = y//i
print(x, y)