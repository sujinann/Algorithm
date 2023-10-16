n = int(input())
s = set()
s.add('ChongChong')
for i in range(n):
    a, b = map(str, input().strip().split())
    if a in s or b in s:
        s.add(a)
        s.add(b)
print(len(s))