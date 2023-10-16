import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
    c = list(input().strip().split())
    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        if len(stack) >= 1:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])