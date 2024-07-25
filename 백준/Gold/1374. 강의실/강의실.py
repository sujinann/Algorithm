n = int(input())

l = []
for i in range(n):
    a, b, c = map(int, input().split())
    l.append([b, c])

l.sort()

answer = [l[0][1]]

for i in range(1, n):
    if answer[0] <= l[i][0]:
        answer[0] = l[i][1]
        answer.sort()
    else:
        answer.append(l[i][1])
        answer.sort()

print(len(answer))