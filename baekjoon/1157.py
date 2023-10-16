N = input().upper()
S = list(set(N))
m = []

for i in S:
    n = N.count(i)
    m.append(n)

if m.count(max(m)) == 1:
    print(S[m.index(max(m))])
else :
    print('?')