X = int(input())
N = int(input())
m = 0
for i in range(1, N + 1) :
    a, b = map(int, input().split())
    m += a*b
if m == X :
    print('Yes')
else :
    print('No')