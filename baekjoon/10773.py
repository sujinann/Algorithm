import sys
input = sys.stdin.readline
k = int(input())
l = []
for i in range(k):
    n = int(input())
    if n != 0:
        l.append(n)
    else:
        del l[len(l)-1]
print(sum(l))