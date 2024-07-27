n = int(input())
l = [[] for i in range(n+1)]
visited = set()

for i in range(n):
    d, r = map(int, input().split())

    l[d].append(r)
    visited.add(d)

visited = list(visited)
visited.sort()

answer = []
for dead in visited:
    answer += l[dead]
    if len(answer) > dead:
        answer.sort()
        answer = answer[len(answer)-dead:]

print(sum(answer))