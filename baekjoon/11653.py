N = int(input())
l = []
while N > 1:
    for i in range(2, 10000000):
        if N % i == 0:
            N = N / i
            l.append(i)
            break
for i in range(len(l)):
    print(l[i])