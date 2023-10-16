import sys
input = sys.stdin.readline
n = int(input())
q = []
cnt = 0
for i in range(1, n+1):
    q.append(i)
while len(q)-1 > cnt:
    for i in range(cnt, len(q)):
        if (i+1) % 2 == 0:
            cnt += 1
            q.append(q[i])
        else:
            cnt += 1
print(q[-1])