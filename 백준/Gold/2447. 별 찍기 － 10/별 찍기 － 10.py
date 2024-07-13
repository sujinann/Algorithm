import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
while n!=1:
    n = n//3
    cnt += 1
temp = '*'
for j in range(cnt):
    l = []
    for i in temp:
        l.append(i*3)
    for i in temp:
        l.append(i+' '*len(temp) +i)
    for i in temp:
        l.append(i*3)
    temp = l
print('\n'.join(temp))