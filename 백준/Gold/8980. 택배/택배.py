import heapq

n, c = map(int, input().split())
m = int(input())

l = []
for i in range(m):
    l.append(list(map(int, input().split())))

l.sort()

hq = []
pre = -1
total = 0
answer = 0
for i in range(m):
    if l[i][0] != pre:
        pre = l[i][0]
        while hq and hq[0][0] <= pre:
            p = heapq.heappop(hq)
            total -= p[1]
            answer += p[1]

    heapq.heappush(hq, [l[i][1], l[i][2]])
    total += l[i][2]

    if total > c:            
        while hq and hq[-1][1] < total - c:
            total -= hq.pop()[1]
            
        if hq:
            hq[-1][1] -= total - c
            total = c

while hq:
    answer += hq.pop()[1]

print(answer)