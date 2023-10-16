N, M = map(int, input().split())
la = []
lb = []
ls = []
for i in range(N):
    a = list(map(int, input().split()))
    for i in a:
        la.append(i)
for i in range(N):
    b = list(map(int, input().split()))
    for i in b:
        lb.append(i)
for i in range(N*M):
    ls.append(la[i]+lb[i])
for p in range(N):
    if p != 0:
        print()    
    for i in range(M*p, M*(p+1)):
        print(ls[i], end=' ')
