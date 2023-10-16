n = int(input())
cnt = 0
s = set()
for i in range(n):
    u = str(input().strip())
    if u == 'ENTER':
        cnt += len(s)
        s = set()
    else:
        s.add(u)
cnt += len(s)
print(cnt)