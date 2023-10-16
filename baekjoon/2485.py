import sys
input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
a = []
for i in range(len(l)-1):
    a.append(l[i+1] - l[i])
m = min(a)
mm = int(m**0.5)
k = [True]*(m+1)
for i in range(2, mm+1):
    if k[i] == True:
        for j in range(i*2, m+1, i):
            k[j] = False
p = [i for i in range(2, m+1) if k[i] == True]
for i in p:
    if all(a)%i == 0:
        a = all(a)//i