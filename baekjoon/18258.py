import sys
input = sys.stdin.readline
q = []
cnt = 0
n = int(input())
for i in range(n):
    c = list(input().rstrip().split())
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'pop':       # 시간초과 https://chancoding.tistory.com/35
        if len(q) > cnt:
            print(q[cnt])
            cnt += 1
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(q)-cnt)
    elif c[0] == 'empty':
        if len(q)-cnt == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(q)-cnt == 0:
            print(-1)
        else:
            print(q[cnt])
    else:
        if len(q)-cnt == 0:
            print(-1)
        else:
            print(q[-1])