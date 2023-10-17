n = int(input())
s = str(n)
l = len(s)

start = 1

if n > 9 * l:
    start = n - (9 * l)

for i in range(start, n+1):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
    if i == n:
        print(0)