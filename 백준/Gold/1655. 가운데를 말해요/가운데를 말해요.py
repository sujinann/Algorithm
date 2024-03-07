import heapq
import sys
input = sys.stdin.readline

n = int(input())
maxh = []
minh = []
for i in range(n):
    temp = int(input())
    if i%2 == 0:
        heapq.heappush(maxh, (-temp, temp))
    else:
        heapq.heappush(minh, (temp, temp))
    if i >= 1:
        if maxh[0][1] > minh[0][1]:
            a = heapq.heappop(maxh)[1]
            b = heapq.heappop(minh)[1]
            heapq.heappush(minh, (a, a))
            heapq.heappush(maxh, (-b, b))
    print(maxh[0][1])