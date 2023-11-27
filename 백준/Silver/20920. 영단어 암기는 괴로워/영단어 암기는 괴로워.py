import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
for i in range(n):
    w = str(input().strip())
    if len(w) >= m:
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1

d = sorted(d.items(), key= lambda x :(-x[1], -len(x[0]), x[0]))
for i in range(len(d)):
    d[i] = list(d[i])
for i in range(len(d)):   
    print(d[i][0])