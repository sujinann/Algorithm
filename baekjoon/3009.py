a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
l1 = [a, c, e]
l2 = [b, d, f]
if l1.count(a) == 1:
    g = a
elif l1.count(c) == 1:
    g = c
else :
    g = e
if l2.count(b) == 1:
    h = b
elif l2.count(d) == 1:
    h = d
else :
    h = f
print(g, h)