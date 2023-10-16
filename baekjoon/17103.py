import sys
input = sys.stdin.readline
l = [True]*(1000001)
l[0] = False
l[1] = False
p = []
for i in range(2, 1001):
    if l[i] == True:
        p.append(i)
        for j in range(2*i, 1000001, i):
            l[j] = False

t = int(input())
for i in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n//2+1):
        if l[i] == True:
            if l[n-i] == True:
                cnt += 1
    print(cnt)