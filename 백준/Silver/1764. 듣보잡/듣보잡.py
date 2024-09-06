import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dh, ds = {}, {}
l1, l2 = [], []
cnt = 0
for i in range(n):
    l1.append(str(input().strip()))
for i in range(m):
    l2.append(str(input().strip()))
for i in l1:
    dh[i] = i
for i in l2:
    if i in dh:
        cnt += 1
        ds[i] = i
print(cnt)
for i in sorted(ds):
    print(i)