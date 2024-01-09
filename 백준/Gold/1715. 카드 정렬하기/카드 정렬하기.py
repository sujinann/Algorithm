import heapq


n = int(input())

q = []
for i in range(n):
    heapq.heappush(q, int(input()))

answer = 0

if n >= 2:
    for i in range(n-1):
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        answer += a + b
        heapq.heappush(q, a+b)

print(answer)