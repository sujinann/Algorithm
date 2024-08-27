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

    if l[i][2] + total > c:
        temp = l[i][2]
        while hq and hq[-1][0] > l[i][1]:
            if temp <= 0:
                break
            
            if temp >= hq[-1][1]:
                t = hq.pop()[1]
                temp -= t
                heapq.heappush(hq, [l[i][1], t])
            else:
                hq[-1][1] -= temp
                heapq.heappush(hq, [l[i][1], temp])
                temp = 0
        else:
            if total < c:
                heapq.heappush(hq, [l[i][1], c-total])
                total = c
    else:
        heapq.heappush(hq, [l[i][1], l[i][2]])
        total += l[i][2]

while hq:
    answer += hq.pop()[1]

print(answer)