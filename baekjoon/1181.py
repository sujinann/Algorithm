n = int(input())
l = []
for i in range(n):
    a = input()
    l.append(a)
s = set(l)
l = list(s)
l.sort()
l.sort(key=len)
for i in l:
    print(i)