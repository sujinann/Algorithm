x, y, w, h = map(int, input().split())
if x < w - x:
    a = x
else :
    a = w - x
if y < h - y:
    b = y
else :
    b = h-y
if a < b :
    print(a)
else :
    print(b)