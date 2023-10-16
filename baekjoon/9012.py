import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    p = input().strip()
    cnt = 0
    for j in p:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            break
    if cnt == 0:
        print('YES')
    else:
        print('NO')