r, l, a = [], [], []

for i in range(5):
    r.append(list(input()))

for i in range(5):
    l.append(len(r[i]))

for i in range(max(l)):
    for p in range(5):
        if i < l[p]:
            a.append(r[p][i])
for i in range(len(a)):
    print(a[i], end='')