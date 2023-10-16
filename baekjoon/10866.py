import sys
input = sys.stdin.readline
n = int(input())
d = []
f = 0
b = 0
for i in range(n):
    c = list(input().split())
    if c[0] == 'push_front':
        d.insert(0, c[1])
    elif c[0] == 'push_back':
        d.append(c[1])
    elif c[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.pop(0)
    elif c[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
    elif c[0] == 'size':
        print(len(d))
    elif c[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    else:
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])