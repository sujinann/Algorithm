import heapq


v, e = map(int, input().split())
q = []
for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, [c, a, b])

l = [i for i in range(v+1)]

def find(x):
    if l[x] != x:
        l[x] = find(l[x])
    return l[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        l[y] = x
    else:
        l[x] = y

answer = 0
cnt = 0

while q:
    c, a, b = heapq.heappop(q)
    if find(a) == find(b):
        continue
    elif a == b:
        continue
    else:
        union(a, b)
        answer += c
        cnt += 1
        if cnt >= v-1:
            break

print(answer)