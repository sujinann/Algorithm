n = int(input())
maps = []
for i in range(n):
    s = str(input())
    maps.append(s)

l, r, b, ll, rr = 0, 0, 0, 0, 0

for i in range(n):
    if '*' in maps[i]:
        for j in range(n):
            if maps[i][j] == '*':
                h = [i, j]

        for k in range(h[1]):
            if maps[h[0]+1][k] == '*':
                l += 1
        
        for k in range(h[1]+1, n):
            if maps[h[0]+1][k] == '*':
                r += 1
            else:
                break

        for k in range(h[0]+2, n):
            if maps[k][h[1]] == '*':
                b += 1
            else:
                break
        
        for k in range(h[0]+2+b, n):
            if maps[k][h[1]-1] == '*':
                ll += 1
            else:
                break
        
        for k in range(h[0]+2+b, n):
            if maps[k][h[1]+1] == '*':
                rr += 1
            else:
                break

        break

print(h[0]+2, h[1]+1)
print(l, r, b, ll, rr)