import sys
input = sys.stdin.readline
n, k = map(int, input().split())
l = []
result = []
cnt = 0
for i in range(1, n+1):
    l.append(i)
while len(result) < n:
    for i in range(cnt, len(l)):
        if (i+1) % k == 0:
            result.append(l[i])
            cnt += 1
        else:
            l.append(l[i])
            cnt += 1
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(result[-1], end='>')