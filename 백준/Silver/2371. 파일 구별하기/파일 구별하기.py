n = int(input())

l = []
maxl = 0
for i in range(n):
    temp = list(map(int, input().split()))
    temp.pop()
    if len(temp) > maxl:
        maxl = len(temp)
    
    l.append(temp)

for i in l:
    if len(i) < maxl:
        i += '0' * (maxl - len(i))

cnt = 0
while True:
    cnt += 1
    s = set()
    for i in range(n):
        s.add(tuple(l[i][:cnt]))

    if len(s) == n:
        break

print(cnt)