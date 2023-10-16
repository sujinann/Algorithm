n = list(map(int, input()))
n.sort()
for i in range(len(n)):
    print(n[len(n)-1-i], end='')