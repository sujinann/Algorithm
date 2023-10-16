B = list(map(int, input().split()))
A = sorted(B)
if A[2] < A[0] + A[1] :
    print(A[0] + A[1] + A[2])
else :
    print((A[0] + A[1]) * 2 - 1)