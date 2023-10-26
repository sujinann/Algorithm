n = int(input())
l = list(map(int, input().split()))
l.sort()

front = []
back = []

for i in range(0, n, 2):
    front.append(l[i])

for i in range(1, n, 2):
    back.append(l[i])
back.sort(reverse=True)

answer = front + back

s = 0
for i in range(n-1):
    s += (answer[i] * answer[i+1])
s += (answer[0] * answer[n-1])

print(s)
print(*answer)