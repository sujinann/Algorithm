import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else :
        d[i] += 1
for i in l2:
    if i in d :
        print(d[i], end=' ')
    else:
        print(0, end=' ')