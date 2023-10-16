S = input()
l = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWXYZ']
cnt = 0

for i in l :
    for j in i :
        for p in S :
            if p == j :
                cnt += l.index(i)+3

print(cnt)