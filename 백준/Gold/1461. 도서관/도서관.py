n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

lcnt = 0
for i in range(n):
    if l[i] < 0:
        lcnt += 1
    else:
        break

rcnt = n - lcnt
r = l[lcnt:]
r.reverse()

dist = []
for i in range(n):
    if i*m + 1 > lcnt:
        break
    dist.append(abs(l[i*m]))

for i in range(n):
    if i*m + 1 > rcnt:
        break
    dist.append(r[i*m])

dist.sort()
answer = 0
for i in range(len(dist)):
    if i == len(dist)-1:
        answer += dist[i]
    else:
        answer += dist[i] * 2

print(answer)