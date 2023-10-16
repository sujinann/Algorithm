a = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']
b = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
S = 0
K = 0

for i in range(20):
    N, M, L = input().split()
    if L == 'P':
        continue
    S += float(M) * b[a.index(L)]
    K += float(M)

print(S / K)