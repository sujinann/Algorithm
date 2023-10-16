N = int(input())
C = 1
A = 0
for i in range(0, 1000000000):
    C += (6 * i)
    A += 1
    if C >= N :
        break
    
print(A)