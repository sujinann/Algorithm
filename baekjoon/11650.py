n = int(input())
l = []
for i in range(n):
    a = list(map(int, input().split()))
    l.append(a)
l.sort()
for i in range(n):
    print(l[i][0], l[i][1])