import sys
input = sys.stdin.readline
l = [True]*(2*123456+1)
l[0] = False
l[1] = False
for i in range(2, int((2*123456)**0.5)+1):
    if l[i] == True :
        for j in range(2*i, 2*123456+1, i):
            l[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = 0
        for i in range(n+1, 2*n+1):
            if l[i] == True:
                a += 1
        print(a)