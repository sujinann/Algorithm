S = input()
L = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

for i in L:
    S = S.replace(i, 'b')

print(len(S))