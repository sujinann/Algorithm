N, M = map(int, input().split())
L = []
A = []
for i in range(N):
    L.append(list(input()))
for p in range(N-7):
    for k in range(M-7):
        a = 0
        b = 0
        for i in range(p, p+8):
            for j in range(k, k+8):
                if (i+j)%2 ==0:
                    if L[i][j] != 'W':
                        a += 1
                    if L[i][j] != 'B':
                        b += 1
                else :
                    if L[i][j] != 'B':
                        a += 1
                    if L[i][j] != 'W':
                        b += 1
        A.append(min(a, b))
print(min(A))