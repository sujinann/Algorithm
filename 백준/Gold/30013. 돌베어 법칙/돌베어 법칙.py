n = int(input())
s = str(input())

term = 1
mini = 2001
while term <= n:
    cnt = 0
    visited = [False] * n
    for i in range(n):
        if s[i] == '#' and not visited[i]:
            cnt += 1
            c = i
            while True:
                if c >= n:
                    break
                if s[c] == '#':
                    visited[c] = True
                    c += term
                else:
                    break
    if cnt < mini:
        mini = cnt
    term += 1

print(mini)