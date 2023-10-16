from collections import deque

n, w, l = map(int, input().split())

truck = deque(list(map(int, input().split())))

q = deque([0]*w)

answer = 0

while q:
    q.popleft()

    if len(truck) > 0:
        if sum(q) + truck[0] > l:
            q.append(0)
        else:
            q.append(truck.popleft())

    answer += 1

print(answer)