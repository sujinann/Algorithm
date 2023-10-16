import sys
input = sys.stdin.readline
m, n = map(int, input().split())
l = [True]*(n+1)
l[0] = [False]
l[1] = [False]
for i in range(2, n+1):
    if l[i] == True:
        for j in range(i*2, n+1, i):
            l[j] = False
for i in range(m, n+1):
    if l[i] == True and i !=1:
        print(i)