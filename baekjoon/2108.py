import sys
input = sys.stdin.readline
l = []
n = int(input())
for i in range(n):
    a = int(input())
    l.append(a)
l.sort()
s = set(l)
p = sum(l)//len(l)
if (sum(l)%len(l))/len(l) >= 0.5:
    p += 1
print(p)
print(l[len(l)//2])
d = {}
for i in s:
    d[i] = l.count(i)
mx = max(d.values())
mxs = []
for i in s:
    if d[i] == mx:
        mxs.append(i)
mxs.sort()
print(mxs[1])
print(max(s)-min(s))