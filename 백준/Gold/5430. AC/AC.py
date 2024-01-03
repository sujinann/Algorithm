import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    p = input().rstrip()
    n = int(input())
    l = list(input().strip()[1:-1].split(','))
    cnt = 0
    e = 0
    if n == 0:
        l = []
    for i in p:
        if i == 'R':
            cnt += 1
        else:
            if len(l) == 0:
                print('error')
                e += 1
                break
            else:
                if cnt % 2 == 0:
                    l.pop(0)
                else:
                    l.pop(-1)
    if cnt % 2 != 0:
        l.reverse()
    if e == 0:
        print('['+','.join(l) +']')