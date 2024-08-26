n, k = map(int, input().split())
m = list(map(int, input().split()))

s = set()

answer = 0
for i in range(k):
    s.add(m[i])
    if len(s) > n:
        s.remove(m[i])
        idx = 0
        target = 0
        for j in s:
            if j in m[i:]:
                idx = max(idx, m[i:].index(j))
            else:
                idx = -1
                target = j
                break
        
        if idx >= 0:
            target = m[i:][idx]

        s.remove(target)
        s.add(m[i])
        answer += 1

print(answer)