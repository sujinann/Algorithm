import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
cnt = 0
while 0 < len(p):
    if (q.index(p[0])+1) <= (len(q)-1)//2+1:
        while p[0] != q[0]:
            q.append(q[0])
            q.pop(0)
            cnt += 1
        q.pop(0)
        p.pop(0)
    else:
        while p[0] != q[0]:
            q.insert(0, q[-1])
            q.pop()
            cnt += 1
        q.pop(0)
        p.pop(0)
print(cnt)