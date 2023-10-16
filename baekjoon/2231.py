N = int(input())
L = len(str(N))
for i in range(1, N+1):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
    if i == N:
        print(0)