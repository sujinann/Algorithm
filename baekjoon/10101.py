A = int(input())
B = int(input())
C = int(input())
if A + B + C == 180 :
    if A == B == 60 :
        print('Equilateral')
    elif A == B or B == C or A == C:
        if A != 60 and B != 60 and C !=60 : #없어도됨 위if중복
            print('Isosceles')
    else :
        print('Scalene')
else :
     print('Error')