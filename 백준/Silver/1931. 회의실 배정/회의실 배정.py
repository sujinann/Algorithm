n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

l.sort(key= lambda x: (x[1], x[0]))
end = -1
answer = 0
for i in l:
    if i[0] >= end:
        answer += 1
        end = i[1]

print(answer)