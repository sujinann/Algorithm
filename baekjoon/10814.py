n = int(input())
l = []
for i in range(n):
    a, b = input().split()
    l.append([int(a), str(b)])
l.sort(key=lambda x:(x[0]))
for i in l:
    print(i[0], i[1])