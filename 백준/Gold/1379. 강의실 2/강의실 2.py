import heapq

n = int(input())
l = []
for i in range(n):
    a, b, c = map(int, input().split())

    l.append([b, c, a])

l.sort(key= lambda x : x[0])
answer = [0] * n

p = [[l[0][1], 1]]
answer[l[0][2]-1] = 1

cnt = 1
for i in range(1, n):
    if p[0][0] <= l[i][0]:
        temp = heapq.heappop(p)
        answer[l[i][2]-1] = temp[1]
        heapq.heappush(p, [l[i][1], temp[1]])
    else:
        cnt += 1
        heapq.heappush(p, [l[i][1], cnt])
        answer[l[i][2]-1] = cnt

print(cnt)
for a in answer:
    print(a)