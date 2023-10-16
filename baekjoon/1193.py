X = int(input())
A = 0
cnt = 0
while A < X :
    cnt += 1
    A += cnt

if cnt % 2 == 0:
    print(f'{cnt-(A-X)}/{A-X+1}')
else :
    print(f'{A-X+1}/{cnt-(A-X)}')