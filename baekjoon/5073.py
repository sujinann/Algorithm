while True:
    A = sorted(list(map(int, input().split())))
    if A[0] == 0 :
        break
    if A[2] < A[0] + A[1] :
        if A[0] == A[1] == A[2] :
            print('Equilateral')
        elif A[0] == A[1] or A[1] == A[2] or A[0] == A[2] :
            print('Isosceles')
        else:
            print('Scalene')
    else :
        print('Invalid')