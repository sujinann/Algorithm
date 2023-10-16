A = []
for i in range(9):
    a = list(map(int, input().split()))
    for i in range(9):
        A.append(a[i])
print(max(A))
if (A.index(max(A))+1)%9 != 0:
    R = ((A.index(max(A))+1)//9)+1
else :
    R = ((A.index(max(A))+1)//9)
if (A.index(max(A))+1)%9 != 0:
    T = (A.index(max(A))+1)%9
else :
    T = 9
print(R, T)